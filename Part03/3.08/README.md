# 3.08 multi-stage frontend

```
docker images --filter reference=*end* 
REPOSITORY              TAG         IMAGE ID      CREATED             SIZE
localhost/3.8-frontend  latest      0b287549997e  9 seconds ago       81.4 MB
localhost/3.7-frontend  latest      c37fdf1a6945  10 minutes ago      533 MB
localhost/3.6-frontend  latest      3d5f23fa606a  26 minutes ago      632 MB
localhost/2.9-frontend  latest      df8f7ae809a2  26 hours ago        1.35 GB
```

```
docker image history 3.8-frontend:latest 
ID            CREATED       CREATED BY                                     SIZE        COMMENT
24ff108bd99b  24 hours ago  /bin/sh -c #(nop) CMD ["serve", "-s", "-l"...  0 B         FROM b764f565a7e9
<missing>     24 hours ago  /bin/sh -c #(nop) USER appuser                 0 B         FROM 24ff108bd99b
<missing>     24 hours ago  /bin/sh -c apk add --no-cache nodejs npm &...  72.6 MB     FROM 92081241d2c3
92081241d2c3  24 hours ago  /bin/sh -c #(nop) COPY dir:43d321358e66067...  1.21 MB     FROM f60be785b42f
c1aabb73d233  24 hours ago  /bin/sh -c #(nop) WORKDIR /app                 0 B         FROM fe0662c7d204
<missing>     24 hours ago  /bin/sh -c #(nop) EXPOSE 5000                  0 B         FROM docker.io/library/alpine:3.18
<missing>     2 days ago    /bin/sh -c #(nop)  CMD ["/bin/sh"]             0 B         
<missing>     2 days ago    /bin/sh -c #(nop) ADD file:1da756d12551a0e...  7.62 MB   
```