FROM ubuntu:20.04

RUN apt-get update && apt-get --yes upgrade && apt-get --yes install curl

WORKDIR /usr/src/app

COPY script.sh .

CMD ./script.sh
