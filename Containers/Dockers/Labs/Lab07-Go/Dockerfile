FROM golang:1.16-alpine

WORKDIR /project/go-docker/

# COPY go.mod, go.sum and download the dependencies
COPY go.* ./
RUN go mod download

# COPY All things inside the project and build
COPY . .
RUN go build -o /project/go-docker/build/myapp .

EXPOSE 8080
ENTRYPOINT [ "/project/go-docker/build/myapp" ]