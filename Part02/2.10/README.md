# 2.10 No exposed ports

The ports were already not exposed in previous exercise. localhost:8080/ping is not accessible.

## nmap localhost

```
Starting Nmap 7.93 ( https://nmap.org ) at 2023-06-10 19:12 EEST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000098s latency).
Other addresses for localhost (not scanned): ::1
Not shown: 999 closed tcp ports (reset)
PORT     STATE     SERVICE
80/tcp   filtered  http

Nmap done: 1 IP address (1 host up) scanned in 0.04 seconds
```