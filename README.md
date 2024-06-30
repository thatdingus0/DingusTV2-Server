# MSN TV 2 Server
A almost functioning MSNTV 2 server.


## How to run
You need python3, Flask, nginx, USB Drive, and this github repo.

## USB Configuration (FOR VERSION 4.3 OR BELOW)
This server isn't a drop-in replacement since the MSN TV 2 requires https to login. 

1. Get a USB Drive formatted in FAT32 
2. Download evalAuto.html and place on your USB 
3. Plug in your usb drive into your MSN TV 2 
4. Open Settings > Choose connection settings > Configure Router 
5. Enter a IP that isn't being used on your network (ex: 192.168.1.274) 
6. Wait for the request to time out 
7. Now enter: msntv://../hard disk/evalAuto.html 

If you see a screen with the text "Configuration Updated" you can click the back button on your keyboard until you reach the login screen \
Now you're ready to connect \
!* NOTE THIS ONLY AFFECT THE CURRENT SESSION, WHEN YOU REBOOT YOU NEED TO DO THIS AGAIN (only steps 4 to 7) *!

## USB Configuration (FOR ANY OTHER VERSION)
This server isn't a drop-in replacement since the MSN TV 2 requires https to login. 

1. Get a USB Drive formatted in FAT32
2. Download configServer.py
3. Run the python script
4. Download evalAuto.html and place on your USB 
5. Plug in your usb drive into your MSN TV 2 
6. Open Settings > Choose connection settings > Configure Router
7. Input your computers IP address

If you see a screen with the text "Configuration Updated" you can click the back button on your keyboard until you reach the login screen \
Now you're ready to connect

!* NOTE THIS ONLY AFFECT THE CURRENT SESSION, WHEN YOU REBOOT YOU NEED TO DO THIS AGAIN (only steps 3 to 7) *!

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

## MSN TV 2 Configuration (Local Server)
First make sure do to the USB Configuration \

1. Open Settings > Choose connection settings > Use proxy servers
2. Find the input "Web Proxy"
3. Input your servers IP address and port (which is 5050)
4. Click done
5. Go back to the login screen
6. And now connect
Done!

## MSN TV 2 Configuration (Global Server)
Coming soon!


## Q/A
### My box isn't connecting (Local/Global)
Make sure that your ethernet cable is plugged in, Dialup isn't supported at this moment. \
Make sure that your firewall isn't blocking your server or the global server.

### The box is still using https or I see a 'Bad Request' error (Local/Global)
Did you make sure to run USB Configuration?  \
This is a required step because there is no way that the MSN TV 2 box will use http normally.

### Is there any hacked image I need to flash?
No, this server uses nginx and USB configuration to bypass HTTPS \
If you have a working HTTPS patch that doesn't require this, Contact me at slost1010s@gmail.com
