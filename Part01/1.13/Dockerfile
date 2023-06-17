FROM golang:1.16

EXPOSE 8080

WORKDIR /app

COPY . .

RUN go build

CMD ["./server"]