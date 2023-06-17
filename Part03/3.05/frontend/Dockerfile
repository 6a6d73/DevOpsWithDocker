FROM node:16

EXPOSE 5000

WORKDIR /app

COPY package*.json .

RUN npm install

COPY . .

RUN npm run build

RUN npm install -g serve

RUN useradd -m appuser

USER appuser

CMD ["serve", "-s", "-l", "5000", "build"]