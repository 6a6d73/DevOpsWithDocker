FROM node:16-alpine AS build-stage

WORKDIR /app

ENV REACT_APP_BACKEND_URL=http://localhost/api/

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

FROM alpine:3.18

EXPOSE 5000

WORKDIR /app

COPY --from=build-stage /app/build /app/build

RUN apk add --no-cache nodejs npm && npm install -g serve && \
    adduser -D appuser && chown --recursive appuser: /app

USER appuser

CMD ["serve", "-s", "-l", "5000", "build"]