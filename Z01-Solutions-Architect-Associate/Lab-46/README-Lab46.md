# AWS Solutions Architect Associate - Laboratorio 46

<br>

### Objetivo: 
* Implementación de Cognito User Pool & Grant Types

### Tópico:
* Security, Identity & Compliance

### Dependencias:
* Ninguna

<br>

---

### A - Implementación de Cognito User Pool

<br>

1. Desde la nueva consola de Cognito (v2), accedemos al servicio "Cognito - User Pools" y damos clic en el botón "Create user pool". Ingresamos/seleccionamos los siguientes valores. Finalmente dar clic en el botón "Create user pool"

  - Authentication providers
    - Provider types: Cognito user pool
    - Cognito user pool sign-in options: Email
  - Password policy
    - Password policy mode: Cognito defaults
  - Multi-factor authentication
    - MFA enforcement: Require MFA - Recommended
    - MFA methods: Authenticator apps
  - User account recovery:
    - Self-service account recovery: Enable self-service account recovery - Recommended
    - Delivery method for user account recovery messages: Email only
  - Self-service sign-up:
    - Self-registration: Enable self-registration
  - Cognito-assisted verification and confirmation:
    - Allow Cognito to automatically send messages to verify and confirm - Recommended
    - Attributes to verify: Send email message, verify email address
  - Verifying attribute changes
    - Keep original attribute value active when an update is pending - Recommended
    - Active attribute values when an update is pending: Email address
  - Required attributes
    - Additional required attributes
      - family_name
      - name
  - Email: Send email with Cognito
  - User pool name:
    - User pool name: Lab46-UserPool
  - Hosted authentication pages: Use the Cognito Hosted UI
  - Domain
    - Domain type: Use a Cognito domain
    - Cognito domain: *Ingrese nombre personalizado* (P.ej.: lab46-userpool)
  - Initial app client
    - App type: Public client
    - App client name: app-client-name
    - Client secret: Generate a client secret
  - Allowed callback URLs: https://google.com/authenticate
 
<br>

<img src="images/Lab46_02.jpg">

<br>

<img src="images/Lab46_03.jpg">

<br>

<img src="images/Lab46_04.jpg">

<br>

<img src="images/Lab46_05.jpg">

<br>

<img src="images/Lab46_06.jpg">

<br>

<img src="images/Lab46_07.jpg">

<br>

<img src="images/Lab46_09.jpg">

<br>

<img src="images/Lab46_10.jpg">

<br>

<img src="images/Lab46_11.jpg">

<br>

<img src="images/Lab46_12.jpg">

<br>

<img src="images/Lab46_13.jpg">

<br>

<img src="images/Lab46_14.jpg">

<br>

<img src="images/Lab46_15.jpg">

<br>

<img src="images/Lab46_16.jpg">

<br>

2. Una vez aprovisionado el recurso, accedemos al detalle del mismo y revisamos las secciones:

  - User pool overview
    * *User pool ID*
  - Users
  - Groups
  - Sign-in experience
    - Password policy
    - Multi-factor authentication
    - User account recovery
  - Sign-up experience
    - Required attributes
    - Self-service sign-up
  - Messaging
  - App integration
    - Configuration for all app clients
      * Cognito domain
    - App client list
      * App clients and analytics
        * *Client ID*
        * *Cliente Secret*
        * *Hosted UI*
  - User pool properties

<br>

<img src="images/Lab46_17.jpg">

<br>

<img src="images/Lab46_18.jpg">

<br>

<img src="images/Lab46_19.jpg">

<br>

<img src="images/Lab46_20.jpg">

<br>


3. Desde la sección, "App Integration" > "App client list" > "App client" > "Hosted UI". Dar clic en el botón "View Hosted UI"

<br>

<img src="images/Lab46_21.jpg">

<br>

4. Aparecerá un login en el cual visualizamos los campos "Email" y "Password". El campo "Email" corresponde a la sección "Sign-in experience > Cognito user pool sign-in > Cognito user pool sign-in options". Damos clic en el enlace "Sign Up".

<br>

<img src="images/Lab46_22.jpg">

<br>

<img src="images/Lab46_23.jpg">

<br>

5. En esta nueva ventana visualizaremos los campos "Email", "Name", "Family Name" y "Password". Los campos "Email", "Name" y "Family Name" corresponden a la sección "Sign-up experience > Required attributes". Ingresamos los valores solicitados y damos clic en el botón "Sign Up"

<br>

<img src="images/Lab46_25.jpg">

<br>

<img src="images/Lab46_24.jpg">

<br>

6. En las dos ventanas descritas anteriormente y en la siguiente, podremos validar que la URL desde donde estamos haciendo estas acciones corresponde al dominio creado en la sección "App Integration > Domain"

<br>

<img src="images/Lab46_26.jpg">

<br>

7. Desde nuestro correo registrado como usuario revisaremos el "Verification code" recibido e ingresamos este valor. Este nuevo paso se activa debido a que durante el proceso de creación se indicó a "Cognito-assisted verification and confirmation" el valor "Send email message, verify email address (Allow Cognito to automatically send messages to verify and confirm - Recommended)"

<br>

<img src="images/Lab46_34.jpg">

<br>

<img src="images/Lab46_27.jpg">

<br>

<img src="images/Lab46_28.jpg">

<br>

8. Se nos redireccionará a la página, por ejemplo: "https://google.com/authenticate?code=df82558b-cc10-46b6-be3a-35a8915e7a7b". Este página corresponde al valor ingresado en la sección "App Integration" > "App client list" > "App client" > "Hosted UI" > "Allowed callback URLs". En esa misma sección se resalta que el campo "OAuth grant types" tiene por contenido "Authorization code grant". La URL generada por "Hosted UI" es, por ejemplo: "https://lab46-userpool.auth.us-east-1.amazoncognito.com/oauth2/authorize?client_id=qgj8h7bej84iksdjtoi2a5vlt&response_type=token&scope=email+openid+phone&redirect_uri=https%3A%2F%2Fgoogle.com%2Fauthenticate" 

<br>

<img src="images/Lab46_29.jpg">

<br>

<img src="images/Lab46_30.jpg">

<br>

9. Editamos la sección "Hosted UI" y modificamos el valor del campo "OAuth 2.0 grant types" por "Implicit gran". Guardamos los cambios y damos clic nuevamente sobre el botón "View Hosted UI". Validaremos que se nos redirecciona a la página, por ejemplo: "https://google.com/authenticate#access_token=eyJraWQiOiJQSkljd2N0ZjNJM2JCUlJoXC81NDIreW0wZkk2TXJQMDVaeG5FSG5pNTFSWT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI1YmEyMTNlZC1iZTg1LTQxZDMtOWJiMS05MjUwZTRhOGMyZjAiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6InBob25lIG9wZW5pZCBlbWFpbCIsImF1dGhfdGltZSI6MTY3OTU0MzY0OCwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tXC91cy1lYXN0LTFfdDFtMnRxb2ZYIiwiZXhwIjoxNjc5NTQ3MjQ4LCJpYXQiOjE2Nzk1NDM2NDgsInZlcnNpb24iOjIsImp0aSI6IjdhMmZkYTViLTRhYTItNDM5OS1iMjlhLWYwMzBlNDg4MWY0ZSIsImNsaWVudF9pZCI6InFnajhoN2Jlajg0aWtzZGp0b2kyYTV2bHQiLCJ1c2VybmFtZSI6IjViYTIxM2VkLWJlODUtNDFkMy05YmIxLTkyNTBlNGE4YzJmMCJ9.Lsy3MfHseOBCbp7bCVDnZU7cMr-9EpRYeuHA-gJoB7nK5ZZtsEGQuFt6U4pEp6-WuZP3RbVrla1tKvh1-KhLfh_VCToO7G_gIuJ3DEZlkFaLpiWLKpnbAS9vvjLByXpMn3vwHlfs-fjLbUxGx_SiJSz51iwy2F3yvuwCTDMcv8UhuynKovY1RhUsTgvXSFqd8yXdlpXpx_HxxBq53KfFSmSdJgk_UhSTvxpCop0UG4Plhm5VFXI6yAVU8xezUVPJRHGYmxWX85JNhKJIVyJv891uZo7mcuxRaxZneaA1ztrn0HChqo8MGpy1A5X2lsaCvPhIgZ3OxajB0c1fmWogpg&id_token=eyJraWQiOiJOUG5ZcFZHVUFlTDVEWGhUcnViWENYakkxNExheXVlNURFdHFzb1ZwKytBPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiV3JlazdNNWI3TExSVmdaREM0QkN1USIsInN1YiI6IjViYTIxM2VkLWJlODUtNDFkMy05YmIxLTkyNTBlNGE4YzJmMCIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV90MW0ydHFvZlgiLCJjb2duaXRvOnVzZXJuYW1lIjoiNWJhMjEzZWQtYmU4NS00MWQzLTliYjEtOTI1MGU0YThjMmYwIiwiYXVkIjoicWdqOGg3YmVqODRpa3NkanRvaTJhNXZsdCIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjc5NTQzNjQ4LCJleHAiOjE2Nzk1NDcyNDgsImlhdCI6MTY3OTU0MzY0OCwianRpIjoiODI5NDkyNDktOWZjNy00Mjk5LTlmZjMtM2MyM2Y3ZTdmNjJhIiwiZW1haWwiOiJqYm8uNzk5MUBnbWFpbC5jb20ifQ.GfbiIOz1UjybIWCJw0YwYolidcB1SnSVwCzMN8d_AZNHuFs2hd37z3EfDud85o5cyn8P33BR2sW3LLbV3ceq_jugsQj2U4D0r6KFiHjxedLNCcKcDgK3kFPyA29Mm7CjnN3EDtjHFf9tDVkj18anBoj3iGjlkH3h7XyzIch27UpcS1xGgdSTKTIGO4V0vxCsgDfC7m1_NTkRlXpmzF-YoxHqA6pC0mJZxbaO8ZUyCxipf6k4o7MqGJpsX7uq5hCCZ7JsM-hOcEGY_hjyvtNTX4l-gyp9QqdMWLOJ9Dwy5VRjJ0y1Rt0JWDXV-LpTx4VHGt4n8Fh42_j6yRAxFAvj8Q&token_type=Bearer&expires_in=3600"

<br>

<img src="images/Lab46_31.jpg">

<br>

<img src="images/Lab46_32.jpg">

<br>

10. Cuando "OAuth grant types" tiene por contenido "Authorization code grant", Cognito nos entrega un "code". Cuando "OAuth grant types" tiene por contenido "Implicit grant", Cognito nos entrega tokens. OAuth 2 proporciona varios "Grant Type" para diferentes casos de uso. Algunos "Grant Type" comúnmente utilizados son:

  * "Authorization code grant" es el método preferido para autorizar a los usuarios finales. En lugar de proporcionar tokens de grupo de usuarios directamente a un usuario final tras la autenticación, se proporciona un código de autorización. Luego, este código se envía a una aplicación personalizada que puede cambiarlo por los tokens deseados. Debido a que los tokens nunca se exponen directamente a un usuario final, es menos probable que se vean comprometidos.

  * Solo use "Implicit grant" cuando haya una razón específica por la que no se puede usar la concesión del código de autorización. En una concesión implícita, los tokens del grupo de usuarios se exponen directamente al usuario final. Como resultado, la identificación y los tokens de acceso tienen más posibilidades de verse comprometidos antes de que caduquen. Por otro lado, si su configuración no contiene ninguna lógica del lado del servidor, es posible que desee utilizar la concesión implícita para evitar que los tokens de actualización se expongan al cliente, ya que la concesión implícita no genera tokens de actualización.

  * "Client credentials grant" es mucho más sencilla que los dos tipos de concesión anteriores. Si bien las concesiones anteriores están destinadas a obtener tokens para los usuarios finales, "Client credentials grant" generalmente tiene como objetivo proporcionar credenciales a una aplicación para autorizar solicitudes de máquina a máquina. Tenga en cuenta que, para usar la concesión de credenciales de cliente, el cliente de aplicación del grupo de usuarios correspondiente debe tener un secreto de cliente de aplicación asociado.

<br>

11. Desde la URL generada, copiamos el contenido de esta e identificamos las secciones "access_token" y "id_token". 

```bash
https://google.com/authenticate#access_token=eyJraWQiOiJQSkljd2N0ZjNJM2JCUlJoXC81NDIreW0wZkk2TXJQMDVaeG5FSG5pNTFSWT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI1YmEyMTNlZC1iZTg1LTQxZDMtOWJiMS05MjUwZTRhOGMyZjAiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6InBob25lIG9wZW5pZCBlbWFpbCIsImF1dGhfdGltZSI6MTY3OTU0MzY0OCwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tXC91cy1lYXN0LTFfdDFtMnRxb2ZYIiwiZXhwIjoxNjc5NTQ3MjQ4LCJpYXQiOjE2Nzk1NDM2NDgsInZlcnNpb24iOjIsImp0aSI6IjdhMmZkYTViLTRhYTItNDM5OS1iMjlhLWYwMzBlNDg4MWY0ZSIsImNsaWVudF9pZCI6InFnajhoN2Jlajg0aWtzZGp0b2kyYTV2bHQiLCJ1c2VybmFtZSI6IjViYTIxM2VkLWJlODUtNDFkMy05YmIxLTkyNTBlNGE4YzJmMCJ9.Lsy3MfHseOBCbp7bCVDnZU7cMr-9EpRYeuHA-gJoB7nK5ZZtsEGQuFt6U4pEp6-WuZP3RbVrla1tKvh1-KhLfh_VCToO7G_gIuJ3DEZlkFaLpiWLKpnbAS9vvjLByXpMn3vwHlfs-fjLbUxGx_SiJSz51iwy2F3yvuwCTDMcv8UhuynKovY1RhUsTgvXSFqd8yXdlpXpx_HxxBq53KfFSmSdJgk_UhSTvxpCop0UG4Plhm5VFXI6yAVU8xezUVPJRHGYmxWX85JNhKJIVyJv891uZo7mcuxRaxZneaA1ztrn0HChqo8MGpy1A5X2lsaCvPhIgZ3OxajB0c1fmWogpg&id_token=eyJraWQiOiJOUG5ZcFZHVUFlTDVEWGhUcnViWENYakkxNExheXVlNURFdHFzb1ZwKytBPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiV3JlazdNNWI3TExSVmdaREM0QkN1USIsInN1YiI6IjViYTIxM2VkLWJlODUtNDFkMy05YmIxLTkyNTBlNGE4YzJmMCIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV90MW0ydHFvZlgiLCJjb2duaXRvOnVzZXJuYW1lIjoiNWJhMjEzZWQtYmU4NS00MWQzLTliYjEtOTI1MGU0YThjMmYwIiwiYXVkIjoicWdqOGg3YmVqODRpa3NkanRvaTJhNXZsdCIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjc5NTQzNjQ4LCJleHAiOjE2Nzk1NDcyNDgsImlhdCI6MTY3OTU0MzY0OCwianRpIjoiODI5NDkyNDktOWZjNy00Mjk5LTlmZjMtM2MyM2Y3ZTdmNjJhIiwiZW1haWwiOiJqYm8uNzk5MUBnbWFpbC5jb20ifQ.GfbiIOz1UjybIWCJw0YwYolidcB1SnSVwCzMN8d_AZNHuFs2hd37z3EfDud85o5cyn8P33BR2sW3LLbV3ceq_jugsQj2U4D0r6KFiHjxedLNCcKcDgK3kFPyA29Mm7CjnN3EDtjHFf9tDVkj18anBoj3iGjlkH3h7XyzIch27UpcS1xGgdSTKTIGO4V0vxCsgDfC7m1_NTkRlXpmzF-YoxHqA6pC0mJZxbaO8ZUyCxipf6k4o7MqGJpsX7uq5hCCZ7JsM-hOcEGY_hjyvtNTX4l-gyp9QqdMWLOJ9Dwy5VRjJ0y1Rt0JWDXV-LpTx4VHGt4n8Fh42_j6yRAxFAvj8Q&token_type=Bearer&expires_in=3600
```
<br>

```bash
access_token=eyJraWQiOiJQSkljd2N0ZjNJM2JCUlJoXC81NDIreW0wZkk2TXJQMDVaeG5FSG5pNTFSWT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI1YmEyMTNlZC1iZTg1LTQxZDMtOWJiMS05MjUwZTRhOGMyZjAiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6InBob25lIG9wZW5pZCBlbWFpbCIsImF1dGhfdGltZSI6MTY3OTU0MzY0OCwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tXC91cy1lYXN0LTFfdDFtMnRxb2ZYIiwiZXhwIjoxNjc5NTQ3MjQ4LCJpYXQiOjE2Nzk1NDM2NDgsInZlcnNpb24iOjIsImp0aSI6IjdhMmZkYTViLTRhYTItNDM5OS1iMjlhLWYwMzBlNDg4MWY0ZSIsImNsaWVudF9pZCI6InFnajhoN2Jlajg0aWtzZGp0b2kyYTV2bHQiLCJ1c2VybmFtZSI6IjViYTIxM2VkLWJlODUtNDFkMy05YmIxLTkyNTBlNGE4YzJmMCJ9.Lsy3MfHseOBCbp7bCVDnZU7cMr-9EpRYeuHA-gJoB7nK5ZZtsEGQuFt6U4pEp6-WuZP3RbVrla1tKvh1-KhLfh_VCToO7G_gIuJ3DEZlkFaLpiWLKpnbAS9vvjLByXpMn3vwHlfs-fjLbUxGx_SiJSz51iwy2F3yvuwCTDMcv8UhuynKovY1RhUsTgvXSFqd8yXdlpXpx_HxxBq53KfFSmSdJgk_UhSTvxpCop0UG4Plhm5VFXI6yAVU8xezUVPJRHGYmxWX85JNhKJIVyJv891uZo7mcuxRaxZneaA1ztrn0HChqo8MGpy1A5X2lsaCvPhIgZ3OxajB0c1fmWogpg
```

<br>

```bash
id_token=eyJraWQiOiJOUG5ZcFZHVUFlTDVEWGhUcnViWENYakkxNExheXVlNURFdHFzb1ZwKytBPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiV3JlazdNNWI3TExSVmdaREM0QkN1USIsInN1YiI6IjViYTIxM2VkLWJlODUtNDFkMy05YmIxLTkyNTBlNGE4YzJmMCIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV90MW0ydHFvZlgiLCJjb2duaXRvOnVzZXJuYW1lIjoiNWJhMjEzZWQtYmU4NS00MWQzLTliYjEtOTI1MGU0YThjMmYwIiwiYXVkIjoicWdqOGg3YmVqODRpa3NkanRvaTJhNXZsdCIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjc5NTQzNjQ4LCJleHAiOjE2Nzk1NDcyNDgsImlhdCI6MTY3OTU0MzY0OCwianRpIjoiODI5NDkyNDktOWZjNy00Mjk5LTlmZjMtM2MyM2Y3ZTdmNjJhIiwiZW1haWwiOiJqYm8uNzk5MUBnbWFpbC5jb20ifQ.GfbiIOz1UjybIWCJw0YwYolidcB1SnSVwCzMN8d_AZNHuFs2hd37z3EfDud85o5cyn8P33BR2sW3LLbV3ceq_jugsQj2U4D0r6KFiHjxedLNCcKcDgK3kFPyA29Mm7CjnN3EDtjHFf9tDVkj18anBoj3iGjlkH3h7XyzIch27UpcS1xGgdSTKTIGO4V0vxCsgDfC7m1_NTkRlXpmzF-YoxHqA6pC0mJZxbaO8ZUyCxipf6k4o7MqGJpsX7uq5hCCZ7JsM-hOcEGY_hjyvtNTX4l-gyp9QqdMWLOJ9Dwy5VRjJ0y1Rt0JWDXV-LpTx4VHGt4n8Fh42_j6yRAxFAvj8Q
```

<br>

12. Desde un terminal Linux o Cloud9 ejecutamos el siguiente comando:

```bash
#Comando Ejemplo - Reemplazar las variables DOMAIN_NAME y ACCESS_TOKEN
curl -X GET https://{$DOMAIN_NAME}h.us-east-1.amazoncognito.com/oauth2/userInfo -H 'Authorization: Bearer {$ACCESS_TOKEN}'

#Comando a ejecutar
curl -X GET https://lab46-userpool.auth.us-east-1.amazoncognito.com/oauth2/userInfo -H 'Authorization: Bearer eyJraWQiOiJQSkljd2N0ZjNJM2JCUlJoXC81NDIreW0wZkk2TXJQMDVaeG5FSG5pNTFSWT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI1YmEyMTNlZC1iZTg1LTQxZDMtOWJiMS05MjUwZTRhOGMyZjAiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6InBob25lIG9wZW5pZCBlbWFpbCIsImF1dGhfdGltZSI6MTY3OTU0MzY0OCwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tXC91cy1lYXN0LTFfdDFtMnRxb2ZYIiwiZXhwIjoxNjc5NTQ3MjQ4LCJpYXQiOjE2Nzk1NDM2NDgsInZlcnNpb24iOjIsImp0aSI6IjdhMmZkYTViLTRhYTItNDM5OS1iMjlhLWYwMzBlNDg4MWY0ZSIsImNsaWVudF9pZCI6InFnajhoN2Jlajg0aWtzZGp0b2kyYTV2bHQiLCJ1c2VybmFtZSI6IjViYTIxM2VkLWJlODUtNDFkMy05YmIxLTkyNTBlNGE4YzJmMCJ9.Lsy3MfHseOBCbp7bCVDnZU7cMr-9EpRYeuHA-gJoB7nK5ZZtsEGQuFt6U4pEp6-WuZP3RbVrla1tKvh1-KhLfh_VCToO7G_gIuJ3DEZlkFaLpiWLKpnbAS9vvjLByXpMn3vwHlfs-fjLbUxGx_SiJSz51iwy2F3yvuwCTDMcv8UhuynKovY1RhUsTgvXSFqd8yXdlpXpx_HxxBq53KfFSmSdJgk_UhSTvxpCop0UG4Plhm5VFXI6yAVU8xezUVPJRHGYmxWX85JNhKJIVyJv891uZo7mcuxRaxZneaA1ztrn0HChqo8MGpy1A5X2lsaCvPhIgZ3OxajB0c1fmWogpg'

#Resultado del comando
{"sub":"5ba213ed-be85-41d3-9bb1-9250e4a8c2f0","email_verified":"true","email":"jXXXXXXX@gmail.com","username":"5ba213ed-be85-41d3-9bb1-9250e4a8c2f0"}
```

<br>

13. Copiamos los valores de los campos "access_token" y "id_token" y los reemplazamos en "https://jwt.io/". Obtendremos los siguientes resultados

```bash
##RESULTADO "access_token"

#HEADER - ALGORITHM & TOKEN TYPE
{
  "kid": "PJIcwctf3I3bBRRh/542+ym0fI6MrP05ZxnEHni51RY=",
  "alg": "RS256"
}

#PAYLOAD - DATA
{
  "sub": "5ba213ed-be85-41d3-9bb1-9250e4a8c2f0",
  "token_use": "access",
  "scope": "phone openid email",
  "auth_time": 1679543648,
  "iss": "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_t1m2tqofX",
  "exp": 1679547248,
  "iat": 1679543648,
  "version": 2,
  "jti": "7a2fda5b-4aa2-4399-b29a-f030e4881f4e",
  "client_id": "qgj8h7bej84iksdjtoi2a5vlt",
  "username": "5ba213ed-be85-41d3-9bb1-9250e4a8c2f0"
}


##RESULTADO "id_token"

#HEADER - ALGORITHM & TOKEN TYPE
{
  "kid": "NPnYpVGUAeL5DXhTrubXCXjI14Layue5DEtqsoVp++A=",
  "alg": "RS256"
}

#PAYLOAD - DATA
{
  "at_hash": "Wrek7M5b7LLRVgZDC4BCuQ",
  "sub": "5ba213ed-be85-41d3-9bb1-9250e4a8c2f0",
  "email_verified": true,
  "iss": "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_t1m2tqofX",
  "cognito:username": "5ba213ed-be85-41d3-9bb1-9250e4a8c2f0",
  "aud": "qgj8h7bej84iksdjtoi2a5vlt",
  "token_use": "id",
  "auth_time": 1679543648,
  "exp": 1679547248,
  "iat": 1679543648,
  "jti": "82949249-9fc7-4299-9ff3-3c23f7e7f62a",
  "email": "jbo.7991@gmail.com"
}
```

<br>

<img src="images/Lab46_35.jpg">

<br>

14. Desde Cognito, accedemos a la sección "Users" y validamos que tenemos un usuario registrado. Desde esta sección podremos generar un usuario. Asimismo desde la "Hosted UI" (Login) podremos modificar la contraseña y realizar otras actividades relacionadas a la gestión del usuario.

<br>

<img src="images/Lab46_33.jpg">

<br>

---

### Eliminación de recursos

```bash
Eliminar "Cognito - User Pool Name"
```

---

### Referencias

 * https://auth0.com/blog/id-token-access-token-what-is-the-difference/
 * https://aws.amazon.com/es/blogs/mobile/understanding-amazon-cognito-user-pool-oauth-2-0-grants/
 * https://dev.to/jinlianwang/setting-up-implicit-grant-workflow-in-aws-cognito-step-by-step-5feg


