# 3.06 optimize frontend and backend

## Summary size comparison

```
podman images --filter reference=*end*
REPOSITORY               TAG         IMAGE ID      CREATED            SIZE
localhost/3.6-backend    latest      4ccd201c1b32  4 minutes ago      629 MB
localhost/3.6-frontend   latest      3d5f23fa606a  6 minutes ago      632 MB
localhost/2.9-frontend   latest      df8f7ae809a2  26 hours ago       1.35 GB
localhost/2.4-backend    latest      b17b32edde07  5 days ago         1.09 GB
```

## Image history

### Frontend before

```
podman image history 2.9-frontend:latest 
ID            CREATED       CREATED BY                                     SIZE              COMMENT
a26c5ae4d6c7  26 hours ago  /bin/sh -c #(nop) CMD ["serve", "-s", "-l"...  0 B               FROM a26c5ae4d6c7
<missing>     26 hours ago  /bin/sh -c npm install -g serve                8.34 MB           FROM 26b4bb400396
26b4bb400396  26 hours ago  /bin/sh -c npm run build                       9.1 MB            FROM e27c016b59b9
6af5664d7fc0  26 hours ago  /bin/sh -c #(nop) ENV REACT_APP_BACKEND_UR...  0 B               FROM 6af5664d7fc0
<missing>     26 hours ago  /bin/sh -c #(nop) COPY dir:6d22a5058e45af9...  732 kB            FROM 1fcef8e50775
1fcef8e50775  5 days ago    /bin/sh -c npm install                         395 MB            FROM bc8b729e19dc
bc8b729e19dc  5 days ago    /bin/sh -c #(nop) COPY multi:58a235c2ed1e7...  696 kB            FROM 75300047e3c0
4fbbe8e45ea1  5 days ago    /bin/sh -c #(nop) WORKDIR /app                 0 B               FROM da42d90e7c3b
<missing>     5 days ago    /bin/sh -c #(nop) EXPOSE 5000                  0 B               FROM docker.io/library/node:16
<missing>     3 weeks ago   /bin/sh -c #(nop)  CMD ["node"]                0 B               
<missing>     3 weeks ago   /bin/sh -c #(nop)  ENTRYPOINT ["docker-ent...  0 B               
<missing>     3 weeks ago   /bin/sh -c #(nop) COPY file:4d192565a7220e...  3.58 kB           
<missing>     3 weeks ago   /bin/sh -c set -ex   && for key in     6A0...  7.61 MB           
<missing>     3 weeks ago   /bin/sh -c #(nop)  ENV YARN_VERSION=1.22.19    0 B               
<missing>     3 weeks ago   /bin/sh -c ARCH= && dpkgArch="$(dpkg --pri...  101 MB            
<missing>     3 weeks ago   /bin/sh -c #(nop)  ENV NODE_VERSION=16.20.0    0 B               
<missing>     3 weeks ago   /bin/sh -c groupadd --gid 1000 node   && u...  350 kB            
<missing>     3 weeks ago   /bin/sh -c set -ex;                            apt-get update;   apt-...     520 MB      
<missing>     3 weeks ago   /bin/sh -c apt-get update && apt-get insta...  150 MB            
<missing>     3 weeks ago   /bin/sh -c set -eux;                           apt-get update;   apt...      34 MB       
<missing>     3 weeks ago   /bin/sh -c #(nop)  CMD ["bash"]                0 B               
<missing>     3 weeks ago   /bin/sh -c #(nop) ADD file:9d769df745075db...  119 MB    
```

### Frontend after

```
podman image history 3.6-frontend:latest 
ID            CREATED       CREATED BY                                     SIZE        COMMENT
c43c9e8d8579  24 hours ago  /bin/sh -c #(nop) CMD ["serve", "-s", "-l"...  0 B         FROM 50f9d4cebb86
<missing>     24 hours ago  /bin/sh -c #(nop) USER appuser                 0 B         FROM c43c9e8d8579
<missing>     24 hours ago  /bin/sh -c apt-get update && apt-get insta...  551 MB      FROM b99254021640
a804cb279a52  24 hours ago  /bin/sh -c #(nop) ENV REACT_APP_BACKEND_UR...  0 B         FROM a804cb279a52
<missing>     24 hours ago  /bin/sh -c #(nop) COPY dir:7be70ab64b006b2...  732 kB      FROM bbd3ae38a218
1f6ddc1b2547  24 hours ago  /bin/sh -c #(nop) WORKDIR /app                 0 B         FROM 25888eea20b7
<missing>     24 hours ago  /bin/sh -c #(nop) EXPOSE 5000                  0 B         FROM docker.io/library/ubuntu:22.04
<missing>     3 weeks ago   /bin/sh -c #(nop)  CMD ["/bin/bash"]           0 B         
<missing>     3 weeks ago   /bin/sh -c #(nop) ADD file:2fd2684e989d275...  80.3 MB     
<missing>     3 weeks ago   /bin/sh -c #(nop)  LABEL org.opencontainer...  0 B         
<missing>     3 weeks ago   /bin/sh -c #(nop)  LABEL org.opencontainer...  0 B         
<missing>     3 weeks ago   /bin/sh -c #(nop)  ARG LAUNCHPAD_BUILD_ARCH    0 B         
<missing>     3 weeks ago   /bin/sh -c #(nop)  ARG RELEASE                 0 B 
```

### Backend before

```
podman image history 2.4-backend:latest 
ID            CREATED        CREATED BY                                     SIZE                      COMMENT
dca3bcf71f3c  5 days ago     /bin/sh -c #(nop) CMD ["./server"]             0 B                       FROM d0dde75b0e6a
<missing>     5 days ago     /bin/sh -c #(nop) ENV REQUEST_ORIGIN=http:...  0 B                       FROM dca3bcf71f3c
<missing>     5 days ago     /bin/sh -c go build                            150 MB                    FROM 70935c5dbaf0
70935c5dbaf0  5 days ago     /bin/sh -c #(nop) COPY dir:3c48a5f24777e30...  43 kB                     FROM 2879880ab86e
972d8c0bc0fc  5 days ago     /bin/sh -c #(nop) WORKDIR /app                 0 B                       FROM cbb674887c1e
<missing>     5 days ago     /bin/sh -c #(nop) EXPOSE 8080                  0 B                       FROM docker.io/library/golang:1.16
<missing>     15 months ago  /bin/sh -c #(nop) WORKDIR /go                  0 B                       
<missing>     15 months ago  /bin/sh -c mkdir -p "$GOPATH/src" "$GOPATH...  3.07 kB                   
<missing>     15 months ago  /bin/sh -c #(nop)  ENV PATH=/go/bin:/usr/l...  0 B                       
<missing>     15 months ago  /bin/sh -c #(nop)  ENV GOPATH=/go              0 B                       
<missing>     15 months ago  /bin/sh -c set -eux;                           arch="$(dpkg --print...   395 MB      
<missing>     15 months ago  /bin/sh -c #(nop)  ENV GOLANG_VERSION=1.16.15  0 B                       
<missing>     15 months ago  /bin/sh -c #(nop)  ENV PATH=/usr/local/go/...  0 B                       
<missing>     15 months ago  /bin/sh -c set -eux;                           apt-get update;           apt...      230 MB      
<missing>     15 months ago  /bin/sh -c apt-get update && apt-get insta...  157 MB                    
<missing>     15 months ago  /bin/sh -c set -ex;                            if ! command -v gpg >...  19.3 MB     
<missing>     15 months ago  /bin/sh -c set -eux;                           apt-get update;           apt...      11.3 MB     
<missing>     15 months ago  /bin/sh -c #(nop)  CMD ["bash"]                0 B                       
<missing>     15 months ago  /bin/sh -c #(nop) ADD file:9c4db2a9644ee30...  129 MB    
```

### Backend after

```
podman image history 3.6-backend:latest 
ID            CREATED       CREATED BY                                     SIZE        COMMENT
47daf64d2158  24 hours ago  /bin/sh -c #(nop) CMD ["./server"]             0 B         FROM 5dca9b353de5
<missing>     24 hours ago  /bin/sh -c #(nop) USER appuser                 0 B         FROM 47daf64d2158
<missing>     24 hours ago  /bin/sh -c apt-get update && apt-get insta...  548 MB      FROM 631f9d7ea26b
23879881265f  24 hours ago  /bin/sh -c #(nop) ENV REQUEST_ORIGIN=http:...  0 B         FROM b294d3644cbd
<missing>     24 hours ago  /bin/sh -c #(nop) ENV PATH "$PATH:/usr/loc...  0 B         FROM 23879881265f
<missing>     24 hours ago  /bin/sh -c #(nop) COPY dir:301c46c92fb07f8...  44 kB       FROM 5f2126b55caf
1f6ddc1b2547  24 hours ago  /bin/sh -c #(nop) WORKDIR /app                 0 B         FROM 127035f3cc89
<missing>     24 hours ago  /bin/sh -c #(nop) EXPOSE 8080                  0 B         FROM docker.io/library/ubuntu:22.04
<missing>     3 weeks ago   /bin/sh -c #(nop)  CMD ["/bin/bash"]           0 B         
<missing>     3 weeks ago   /bin/sh -c #(nop) ADD file:2fd2684e989d275...  80.3 MB     
<missing>     3 weeks ago   /bin/sh -c #(nop)  LABEL org.opencontainer...  0 B         
<missing>     3 weeks ago   /bin/sh -c #(nop)  LABEL org.opencontainer...  0 B         
<missing>     3 weeks ago   /bin/sh -c #(nop)  ARG LAUNCHPAD_BUILD_ARCH    0 B         
<missing>     3 weeks ago   /bin/sh -c #(nop)  ARG RELEASE                 0 B  
```