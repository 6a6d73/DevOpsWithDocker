# 1.16 Cloud development

The app is available at: https://c2ac03f-e0e6-4f8a-b19f-8f9aaf-98caff9048b7.herokuapp.com/

## Setup

First [install Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), then:

Log into Heroku:

```
heroku login
```

Sign into [Container Registry](https://devcenter.heroku.com/articles/container-registry-and-runtime):

```
heroku container:login
```

Create API Token

```
heroku authorizations:create --short
8f61c448-0492-4828-abe0-7c9904969afc # Not real, so do not even think about it.
```

Create app

```
heroku apps:create c2ac03f-e0e6-4f8a-b19f-8f9aaf --region eu
```

[Push existing image](https://devcenter.heroku.com/articles/container-registry-and-runtime#pushing-an-existing-image):

```
docker tag devopsdockeruh/coursepage:latest registry.heroku.com/c2ac03f-e0e6-4f8a-b19f-8f9aaf/web
docker push registry.heroku.com/c2ac03f-e0e6-4f8a-b19f-8f9aaf/web
heroku container:release web --app c2ac03f-e0e6-4f8a-b19f-8f9aaf
```

Get URL for web-app:

```
heroku apps:info c2ac03f-e0e6-4f8a-b19f-8f9aaf
=== c2ac03f-e0e6-4f8a-b19f-8f9aaf
Web URL:        https://c2ac03f-e0e6-4f8a-b19f-8f9aaf-98caff9048b7.herokuapp.com/
```

### Heroku hurdles

In order to get the web-app up and running with Heroku there were a few loops to jump through with Heroku. Had to add a credit card for the free student plan, that has changed since the course material was written. Took a while to even be able to submit the form, was greeted with 'Retry later' for a few days. Once it finally, was submitted had to wait a few days for credits to appear.

## Dockerfile

The instructions for 1.16 exercise say that if we do not have our own web-app, that we may use the course material. That is what I have done. It also says to submit the Dockerfile. The link to the Dockerfile is here: https://github.com/docker-hy/docker-hy.github.io/blob/master/Dockerfile