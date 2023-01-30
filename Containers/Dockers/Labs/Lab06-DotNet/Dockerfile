FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /src

# These lines copy MvcMovie.csproj project files in the current directory 
# and then restore for the specified runtime, using -r.
COPY ["MvcMovie.csproj", "./"]
RUN dotnet restore "MvcMovie.csproj" -r linux-musl-arm64

# Build dotnet project and publishes the application and its dependencies to a folder for deployment to a hosting system.
COPY . .
WORKDIR "/src/."
RUN dotnet publish "MvcMovie.csproj" -c Release -o /app/publish -r linux-musl-arm64 --self-contained false --no-restore

# Docker build command
# You need to use an architecture-specific tag if you want to target ARM based instances. 
# Note that .NET is only supported on Alpine on ARM64 and x64, and not ARM32.
FROM mcr.microsoft.com/dotnet/aspnet:5.0-alpine-arm64v8
WORKDIR /app
EXPOSE 80
COPY --from=build /app/publish .
ENTRYPOINT ["dotnet", "MvcMovie.dll"]