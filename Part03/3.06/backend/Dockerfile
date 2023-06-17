FROM ubuntu:22.04

EXPOSE 8080

WORKDIR /app

COPY . .

ENV PATH "$PATH:/usr/local/go/bin"

ENV REQUEST_ORIGIN=http://localhost:5000

RUN apt-get update && apt-get install --yes curl && \
    curl -O -L "https://go.dev/dl/go1.16.15.linux-amd64.tar.gz" \
    && tar -C /usr/local -xzf go1.16.15.linux-amd64.tar.gz && \
    rm ./go1.16.15.linux-amd64.tar.gz && \
    apt-get purge --yes --auto-remove curl && \
    rm -rf /var/lib/apt/lists/* && go build && useradd -m appuser

USER appuser

CMD ["./server"]