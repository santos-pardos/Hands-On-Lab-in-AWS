using System.Collections.Generic;
using System.Text.Json;
using System.Text.Json.Serialization; // <-- IMPORTANTE
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using Amazon.Lambda.Serialization.SystemTextJson;

[assembly: LambdaSerializer(typeof(SourceGeneratorLambdaJsonSerializer<HolaMundo.LambdaJsonContext>))]

namespace HolaMundo;

public class Function
{
    public APIGatewayProxyResponse FunctionHandler(APIGatewayProxyRequest request, ILambdaContext context)
    {
        var bodyObj = new
        {
            mensaje = "Hola mundo desde Lambda (.NET) 👋",
            metodo = request?.HttpMethod,
            path = request?.Path
        };

        return new APIGatewayProxyResponse
        {
            StatusCode = 200,
            Headers = new Dictionary<string, string>
            {
                ["Content-Type"] = "application/json"
            },
            Body = JsonSerializer.Serialize(bodyObj)
        };
    }
}

[JsonSerializable(typeof(APIGatewayProxyRequest))]
[JsonSerializable(typeof(APIGatewayProxyResponse))]
public partial class LambdaJsonContext : JsonSerializerContext
{
}
