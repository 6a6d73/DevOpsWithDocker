# 3.10 optimize own image

```
docker images --filter reference=*3.10*
REPOSITORY             TAG         IMAGE ID      CREATED       SIZE
localhost/3.10-after   latest      e16e78e698a8  24 hours ago  4.9 MB
localhost/3.10-before  latest      2cd0890365c4  24 hours ago  938 MB
```

```
docker image history 3.10-before:latest 
ID            CREATED       CREATED BY                                     SIZE                     COMMENT
9ac69952ec69  24 hours ago  /bin/sh -c #(nop) ENTRYPOINT ["./go_curl"]     0 B                      FROM 9ac69952ec69
<missing>     24 hours ago  /bin/sh -c go build                            69.3 MB                  FROM d862c3ef69a3
d862c3ef69a3  24 hours ago  /bin/sh -c #(nop) COPY multi:e14dcd592db5e...  4.1 kB                   FROM 5ea571eb534a
e5ba91fc310d  24 hours ago  /bin/sh -c #(nop) WORKDIR /app                 0 B                      FROM docker.io/library/golang:1.20
<missing>     2 days ago    /bin/sh -c #(nop) WORKDIR /go                  0 B                      
<missing>     2 days ago    /bin/sh -c mkdir -p "$GOPATH/src" "$GOPATH...  3.07 kB                  
<missing>     2 days ago    /bin/sh -c #(nop)  ENV PATH=/go/bin:/usr/l...  0 B                      
<missing>     2 days ago    /bin/sh -c #(nop)  ENV GOPATH=/go              0 B                      
<missing>     2 days ago    /bin/sh -c set -eux;                           arch="$(dpkg --print...  254 MB      
<missing>     2 days ago    /bin/sh -c #(nop)  ENV GOLANG_VERSION=1.20.5   0 B                      
<missing>     2 days ago    /bin/sh -c #(nop)  ENV PATH=/usr/local/go/...  0 B                      
<missing>     2 days ago    /bin/sh -c set -eux;                           apt-get update;          apt...      262 MB      
<missing>     4 days ago    /bin/sh -c apt-get update && apt-get insta...  181 MB                   
<missing>     4 days ago    /bin/sh -c set -eux;                           apt-get update;          apt...      49.6 MB     
<missing>     4 days ago    /bin/sh -c #(nop)  CMD ["bash"]                0 B                      
<missing>     4 days ago    /bin/sh -c #(nop) ADD file:98cacc5890a8c0b...  121 MB    
```

```
docker image history 3.10-after:latest 
ID            CREATED       CREATED BY                                     SIZE        COMMENT
facb44374498  24 hours ago  /bin/sh -c #(nop) ENTRYPOINT ["./go_curl"]     0 B         FROM 8cbbd50e6c31
<missing>     24 hours ago  /bin/sh -c #(nop) USER 65534:65534             0 B         FROM facb44374498
<missing>     24 hours ago  /bin/sh -c #(nop) COPY file:13fb3182670ab5...  4.68 MB     FROM 46e4e870a533
46e4e870a533  24 hours ago  /bin/sh -c #(nop) COPY file:cdf7927205f846...  218 kB      FROM 271f05016a78
<missing>     24 hours ago  /bin/sh -c #(nop) WORKDIR /app                 0 B  
```