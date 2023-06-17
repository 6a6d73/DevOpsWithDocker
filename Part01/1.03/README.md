# 1.3 Secret message

Secret message is: 'You can find the source code here: https://github.com/docker-hy'

```
docker run --detach --name secret_message devopsdockeruh/simple-web-service:ubuntu
docker exec --interactive --tty secret_message bash
root@685f8718f72d:/usr/src/app# tail -f ./text.log 
2023-04-27 11:18:50 +0000 UTC
Secret message is: 'You can find the source code here: https://github.com/docker-hy'
2023-04-27 11:18:52 +0000 UTC
```
