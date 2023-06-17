FROM ubuntu:18.04

EXPOSE 5000

WORKDIR /app

COPY . .

ENV REACT_APP_BACKEND_URL=http://localhost/api/

RUN apt-get update && apt-get install --yes curl && \
    curl -sL https://deb.nodesource.com/setup_16.x | bash && \
    apt-get install --yes nodejs && npm install && \
    npm run build && npm install -g serve && \
    apt-get purge --yes --auto-remove curl && \
    rm -rf /var/lib/apt/lists/* && useradd -m appuser

USER appuser

CMD ["serve", "-s", "-l", "5000", "build"]