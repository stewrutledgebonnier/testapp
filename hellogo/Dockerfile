FROM golang:1.8
WORKDIR /go/src/hellogo
COPY . .

RUN GOOS=linux go build -v ./...
