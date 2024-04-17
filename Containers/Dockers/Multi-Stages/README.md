## Multi Stages with React
```
npx create-react-app app — template typescript
```
```
FROM node:18
WORKDIR /app
COPY app /app
RUN npm install -g webserver.local
RUN npm install && npm run build

EXPOSE 3000
CMD webserver.local -d ./build
```
```
FROM node:18-alpine
WORKDIR /app
COPY app /app
RUN npm install -g webserver.local
RUN npm install && npm run build
EXPOSE 3000
CMD webserver.local -d ./build
```
```
FROM node:18-alpine AS build
WORKDIR /app
COPY app /app
RUN npm install && npm run build

FROM node:18-alpine
WORKDIR /app
RUN npm install -g webserver.local
COPY --from=build /app/build ./build
EXPOSE 3000
CMD webserver.local -d ./build
```
```
FROM node:18-alpine AS build
WORKDIR /app
COPY app /app
RUN npm install && npm run build

FROM nginx:stable-alpine
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

## Links
```
https://jonathansandovalf.medium.com/optimizaci%C3%B3n-de-imagen-de-docker-de-1-16-gb-a-22-4-mb-5b190be4eb02
```
