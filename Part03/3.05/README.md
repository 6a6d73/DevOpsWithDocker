# 3.05 non-root user

Using the below command shows that the new Dockerfiles have taken effect and the containers start their processes as non-root user 'appuser'.

```
# before switching users
docker inspect $(docker ps -q) --format '{{.Config.User}} {{.Name}}'
 trusting_payne
 gracious_ellis

# after switching users
docker inspect $(docker ps -q) --format '{{.Config.User}} {{.Name}}'
appuser optimistic_jang
appuser quirky_bartik
```