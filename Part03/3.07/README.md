# 3.07 optimize with alpine

## Summary size comparison

```
docker images --filter reference=*end* 
REPOSITORY              TAG         IMAGE ID      CREATED             SIZE
localhost/3.7-backend   latest      c1beac5a97d5  About a minute ago  461 MB
localhost/3.7-frontend  latest      c37fdf1a6945  2 minutes ago       533 MB
localhost/3.6-backend   latest      4ccd201c1b32  16 minutes ago      629 MB
localhost/3.6-frontend  latest      3d5f23fa606a  18 minutes ago      632 MB
localhost/2.9-frontend  latest      df8f7ae809a2  26 hours ago        1.35 GB
localhost/2.4-backend   latest      b17b32edde07  5 days ago          1.09 GB
```

## After image history

Check previous exercise for comparisons to older versions

### Frontend after

```
docker image history 3.7-frontend:latest 
ID            CREATED       CREATED BY                                     SIZE        COMMENT
934cf3ae0828  24 hours ago  /bin/sh -c #(nop) CMD ["serve", "-s", "-l"...  0 B         FROM e07ea8f2c1aa
<missing>     24 hours ago  /bin/sh -c #(nop) USER appuser                 0 B         FROM 934cf3ae0828
<missing>     24 hours ago  /bin/sh -c npm install && npm run build &&...  412 MB      FROM 4e07f78b4bce
fe581faf7f7a  24 hours ago  /bin/sh -c #(nop) ENV REACT_APP_BACKEND_UR...  0 B         FROM fe581faf7f7a
<missing>     24 hours ago  /bin/sh -c #(nop) COPY dir:8e44f0358a5b1e6...  733 kB      FROM af6c3c66ad5f
4874253f493b  24 hours ago  /bin/sh -c #(nop) WORKDIR /app                 0 B         FROM 82405ce9d836
<missing>     24 hours ago  /bin/sh -c #(nop) EXPOSE 5000                  0 B         FROM docker.io/library/node:16-alpine
<missing>     2 days ago    /bin/sh -c #(nop)  CMD ["node"]                0 B         
<missing>     2 days ago    /bin/sh -c #(nop)  ENTRYPOINT ["docker-ent...  0 B         
<missing>     2 days ago    /bin/sh -c #(nop) COPY file:4d192565a7220e...  3.58 kB     
<missing>     2 days ago    /bin/sh -c apk add --no-cache --virtual .b...  7.79 MB     
<missing>     2 days ago    /bin/sh -c #(nop)  ENV YARN_VERSION=1.22.19    0 B         
<missing>     2 days ago    /bin/sh -c addgroup -g 1000 node     && ad...  105 MB      
c1aabb73d233  2 days ago    /bin/sh -c #(nop)  ENV NODE_VERSION=16.20.0    0 B         
<missing>     2 days ago    /bin/sh -c #(nop)  CMD ["/bin/sh"]             0 B         
<missing>     2 days ago    /bin/sh -c #(nop) ADD file:1da756d12551a0e...  7.62 MB     
```

### Backend after

```
docker image history 3.7-backend:latest 
ID            CREATED        CREATED BY                                     SIZE                     COMMENT
396a7b4bac5c  24 hours ago   /bin/sh -c #(nop) CMD ["./server"]             0 B                      FROM a942770ae355
<missing>     24 hours ago   /bin/sh -c #(nop) USER appuser                 0 B                      FROM 396a7b4bac5c
<missing>     24 hours ago   /bin/sh -c go build && adduser -D appuser      150 MB                   FROM cd51e140b9bb
6782dd7a75e7  24 hours ago   /bin/sh -c #(nop) ENV REQUEST_ORIGIN=http:...  0 B                      FROM 6782dd7a75e7
<missing>     24 hours ago   /bin/sh -c #(nop) COPY dir:59a8d1382cfd320...  45.1 kB                  FROM d8c0b0fb0511
7642119cd161  24 hours ago   /bin/sh -c #(nop) WORKDIR /app                 0 B                      FROM 558168524377
<missing>     24 hours ago   /bin/sh -c #(nop) EXPOSE 8080                  0 B                      FROM docker.io/library/golang:1.16-alpine3.15
<missing>     15 months ago  /bin/sh -c #(nop) WORKDIR /go                  0 B                      
<missing>     15 months ago  /bin/sh -c mkdir -p "$GOPATH/src" "$GOPATH...  3.07 kB                  
<missing>     15 months ago  /bin/sh -c #(nop)  ENV PATH=/go/bin:/usr/l...  0 B                      
<missing>     15 months ago  /bin/sh -c #(nop)  ENV GOPATH=/go              0 B                      
<missing>     15 months ago  /bin/sh -c set -eux;                           apk add --no-cache -...  304 MB      
<missing>     15 months ago  /bin/sh -c #(nop)  ENV GOLANG_VERSION=1.16.15  0 B                      
<missing>     18 months ago  /bin/sh -c #(nop)  ENV PATH=/usr/local/go/...  0 B                      
<missing>     18 months ago  /bin/sh -c [ ! -e /etc/nsswitch.conf ] && ...  2.56 kB                  
<missing>     18 months ago  /bin/sh -c apk add --no-cache ca-certificates  769 kB                   
<missing>     18 months ago  /bin/sh -c #(nop)  CMD ["/bin/sh"]             0 B                      
<missing>     18 months ago  /bin/sh -c #(nop) ADD file:9233f6f2237d796...  5.87 MB 
```