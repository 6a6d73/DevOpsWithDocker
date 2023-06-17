# 1.09 Volumes

```
touch text.log
docker run --rm --volume "$(pwd)/text.log:/usr/src/app/text.log:Z" devopsdockeruh/simple-web-service
^C

tail -4 text.log
2023-04-30 09:36:57 +0000 UTC
Secret message is: 'You can find the source code here: https://github.com/docker-hy'
2023-04-30 09:36:59 +0000 UTC
2023-04-30 09:37:01 +0000 UTC
```