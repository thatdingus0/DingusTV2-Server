# MSN TV 2 Server
A almost functioning MSNTV 2 server.

## How to run
You need python3, Flask, nginx, and this github repo.

## Installing required packages
### Linux
Open a terminal
- Arch
  `sudo pacman -Sy python3`
- Ubuntu
  `sudo apt update && sudo apt install -y python3`

### Windows
Go to https://www.python.org/downloads/ \
And download the latest version

### Linux
- Arch \
  `sudo pacman -Sy nginx` \
  `sudo pacman -Sy python-flask`
- Ubuntu \
  `sudo apt install nginx` \
  `sudo pip3 install Flask`

### Windows
Open a browser \
Goto: https://nginx.org/en/download.html (Place in the C:/ drive) \ 
And download the latest version
Open command prompt \
Run `python -m pip install Flask` or `pip install Flask`

## NGINX configuration

### Linux
Open a terminal
Run: `nano /etc/nginx` or use vim.

### Windows
Open notepad
File > Open
C:/nginx/conf and look for nginx.conf

### Copy this config


```#user  nobody;
worker_processes  1;

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;


events {
    worker_connections  1024;
}

http {
server_names_hash_bucket_size 64;  # Increase this value
    upstream backend_80 {
        server 192.168.1.58:80;
    }

    upstream backend_82 {
        server 192.168.1.58:82;
    }

    server {
        listen 5050;
        server_name sg1.trusted.msntv.msn.com sg2.trusted.msntv.msn.com sg3.trusted.msntv.msn.com sg4.trusted.msntv.msn.com headwaiter.trusted.msntv.msn.com headwaiter.msntv.msn.com;

        location / {
            proxy_pass http://backend_80;
        }
    }

    server {
        listen 5050;
        server_name msntv.msn.com;

        location / {
            proxy_pass http://backend_82;
        }
    }
}

```
Make sure to change 192.168.1.58 to your server ip.


