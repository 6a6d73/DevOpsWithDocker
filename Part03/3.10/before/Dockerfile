FROM golang:1.20

WORKDIR /app

COPY curl.go go.mod ./

RUN go build

ENTRYPOINT ["./go_curl"]