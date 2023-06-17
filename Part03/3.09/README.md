# 3.09 multi-stage backend

```
docker images --filter reference=*end* 
REPOSITORY              TAG         IMAGE ID      CREATED             SIZE
localhost/3.9-backend   latest      0cb460633c16  About a minute ago  13.1 MB
localhost/3.7-backend   latest      c1beac5a97d5  9 minutes ago       461 MB
localhost/3.6-backend   latest      4ccd201c1b32  24 minutes ago      629 MB
localhost/2.4-backend   latest      b17b32edde07  5 days ago          1.09 GB
```

```
docker image history 3.9-backend:latest 
ID            CREATED       CREATED BY                                     SIZE        COMMENT
d04d0474ec31  24 hours ago  /bin/sh -c #(nop) CMD ["./server"]             0 B         FROM 4b6cf65180b6
<missing>     24 hours ago  /bin/sh -c #(nop) USER 65534:65534             0 B         FROM d04d0474ec31
<missing>     24 hours ago  /bin/sh -c #(nop) COPY file:a7428bb6c26dab...  13.1 MB     FROM bd5b7a589dae
<missing>     24 hours ago  /bin/sh -c #(nop) WORKDIR /app                 0 B         FROM 3b600d484450
<missing>     24 hours ago  /bin/sh -c #(nop) EXPOSE 8080                  0 B     
```