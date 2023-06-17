FROM docker:latest

WORKDIR /tmp

RUN apk update && apk add git uuidgen

COPY builder.sh .

ENTRYPOINT [ "./builder.sh" ]