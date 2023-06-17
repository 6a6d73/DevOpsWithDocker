FROM golang:1.16 AS build-stage

WORKDIR /app

COPY . .

ENV REQUEST_ORIGIN=http://localhost:5000

ENV CGO_ENABLED=0

RUN go build -ldflags "-s -w"

FROM scratch

EXPOSE 8080

WORKDIR /app

COPY --from=build-stage /app/server /app

USER 65534:65534

CMD ["./server"]