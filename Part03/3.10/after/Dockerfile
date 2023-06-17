FROM golang:1.20 AS build-stage

WORKDIR /app

RUN apt-get update && apt-get install --yes ca-certificates

COPY curl.go go.mod ./

ENV CGO_ENABLED=0

RUN go build -ldflags "-s -w"

FROM scratch

WORKDIR /app

COPY --from=build-stage /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/

COPY --from=build-stage /app/go_curl /app

USER 65534:65534

ENTRYPOINT ["./go_curl"]