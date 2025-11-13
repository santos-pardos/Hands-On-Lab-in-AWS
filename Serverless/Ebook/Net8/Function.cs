using System;
using System.Collections.Generic;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Threading.Tasks;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.DocumentModel;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using Amazon.SimpleNotificationService;
using Amazon.SimpleNotificationService.Model;

// Necesario para que Lambda use este serializer si lo necesitas en otros casos
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace LambdaSnsDdb
{
    public class Function
    {
        // Ajusta la región si tu Lambda está en otra
        private static readonly IAmazonSimpleNotificationService SnsClient =
            new AmazonSimpleNotificationServiceClient();

        private static readonly IAmazonDynamoDB DynamoClient =
            new AmazonDynamoDBClient();

        // Igual que en tu Python
        private const string SnsTopicArn = "arn:aws:sns:us-east-1:883822223160:S3-CV-SNS";
        private const string DdbTableName = "ContactMessages";

        private static readonly JsonSerializerOptions JsonOptions = new()
        {
            PropertyNamingPolicy = JsonNamingPolicy.CamelCase,
            DefaultIgnoreCondition = JsonIgnoreCondition.WhenWritingNull,
            WriteIndented = false
        };

        private static readonly Dictionary<string, string> CorsHeaders = new()
        {
            ["Access-Control-Allow-Origin"] = "*",
            ["Access-Control-Allow-Headers"] = "Content-Type",
            ["Access-Control-Allow-Methods"] = "POST, OPTIONS",
            ["Content-Type"] = "application/json"
        };

        public async Task<APIGatewayProxyResponse> FunctionHandler(
            APIGatewayProxyRequest request,
            ILambdaContext context)
        {
            // CORS preflight
            if (string.Equals(request.HttpMethod, "OPTIONS", StringComparison.OrdinalIgnoreCase))
            {
                return new APIGatewayProxyResponse
                {
                    StatusCode = 200,
                    Headers = CorsHeaders,
                    Body = string.Empty
                };
            }

            try
            {
                var body = ParseBody(request.Body);

                var name = (body.Name ?? string.Empty).Trim();
                var email = (body.Email ?? string.Empty).Trim();
                var phone = (body.Phone ?? string.Empty).Trim();
                var message = (body.Message ?? string.Empty).Trim();

                // Validación de obligatorios
                if (string.IsNullOrWhiteSpace(name) || string.IsNullOrWhiteSpace(email))
                {
                    return ErrorResponse(400, "Los campos name y email son obligatorios");
                }

                // Validación básica de email
                if (!IsValidEmail(email))
                {
                    return ErrorResponse(400, "El formato del email no es válido");
                }

                var timestamp = DateTime.UtcNow.ToString("o");

                var snsMessage = new
                {
                    name,
                    email,
                    phone = string.IsNullOrWhiteSpace(phone) ? "N/A" : phone,
                    message = string.IsNullOrWhiteSpace(message) ? "Solicitud de descarga de ebook" : message,
                    timestamp
                };

                // === 1) Guardar en DynamoDB ===
                var table = Table.LoadTable(DynamoClient, DdbTableName);

                var item = new Document
                {
                    ["id"] = Guid.NewGuid().ToString(), // PK string
                    ["name"] = snsMessage.name,
                    ["email"] = snsMessage.email,
                    ["phone"] = snsMessage.phone,
                    ["message"] = snsMessage.message,
                    ["timestamp"] = snsMessage.timestamp
                };

                await table.PutItemAsync(item);

                // === 2) Publicar en SNS ===
                var snsPayload = JsonSerializer.Serialize(snsMessage, JsonOptions);

                await SnsClient.PublishAsync(new PublishRequest
                {
                    TopicArn = SnsTopicArn,
                    Subject = $"Nueva solicitud de ebook - {name}",
                    Message = snsPayload
                });

                var okBody = JsonSerializer.Serialize(
                    new { success = true, message = "Solicitud enviada correctamente" },
                    JsonOptions
                );

                return new APIGatewayProxyResponse
                {
                    StatusCode = 200,
                    Headers = CorsHeaders,
                    Body = okBody
                };
            }
            catch (JsonException)
            {
                return ErrorResponse(400, "Formato JSON inválido");
            }
            catch (Exception ex)
            {
                return ErrorResponse(500, "Error al procesar la solicitud", ex.Message);
            }
        }

        private static BodyDto ParseBody(string? body)
        {
            if (string.IsNullOrWhiteSpace(body))
            {
                return new BodyDto();
            }

            return JsonSerializer.Deserialize<BodyDto>(body, JsonOptions) ?? new BodyDto();
        }

        private static bool IsValidEmail(string email)
        {
            // Igual de simple que en Python: contiene @ y un punto en la parte de dominio
            var atIndex = email.IndexOf('@');
            if (atIndex <= 0 || atIndex == email.Length - 1)
            {
                return false;
            }

            var domainPart = email[(atIndex + 1)..];
            return domainPart.Contains('.');
        }

        private static APIGatewayProxyResponse ErrorResponse(int statusCode, string message, string? details = null)
        {
            var obj = details == null
                ? new { error = message }
                : new { error = message, details };

            var body = JsonSerializer.Serialize(obj, JsonOptions);

            return new APIGatewayProxyResponse
            {
                StatusCode = statusCode,
                Headers = CorsHeaders,
                Body = body
            };
        }

        private class BodyDto
        {
            // Mapea name, email, phone, message del JSON
            public string? Name { get; set; }
            public string? Email { get; set; }
            public string? Phone { get; set; }
            public string? Message { get; set; }
        }
    }
}

