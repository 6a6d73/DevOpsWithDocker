#!/bin/sh

git_repo=${1}
docker_repo=${2}
dl_location="/tmp/$(uuidgen)"

git clone ${git_repo} ${dl_location}

docker build ${dl_location} --tag ${docker_repo}

docker push ${docker_repo}