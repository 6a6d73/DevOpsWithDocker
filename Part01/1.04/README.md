# 1.4 Install missing dependencies

```
docker run --rm --interactive --tty --name no_curl ubuntu:latest sh -c 'apt-get update; apt-get install --yes curl;read -p "Input website:" website; echo "Searching.."; sleep 1; curl http://$website'
```

## Alternative

Open a second terminal and install curl. Then when the website is input, will work as above.

```
run --rm --interactive --tty --name no_curl ubuntu:latest sh -c 'while true; do echo "Input website:"; read website; echo "Searching.."; sleep 1; curl http://$website; done'
Input website:
helsinki.fi
Searching..
<html>
<head><title>301 Moved Permanently</title></head>
<body>
<center><h1>301 Moved Permanently</h1></center>
<hr><center>nginx/1.20.1</center>
</body>
</html>
```

```
docker exec --interactive --tty no_curl bash
apt update
apt install --yes curl
```
