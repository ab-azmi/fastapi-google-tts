# Text To Speech Server with gTTS and FastAPI

# -------------[ Setup Backend ]---------------
## Prerequisites

- Ubuntu 20.04 or later
- Python 3.8 or later


## Step 1: Update and Upgrade the System

First, update and upgrade your system packages:

```sh
sudo apt update
sudo apt upgrade -y
```

## Step 2: Install Python
Install Python and pip
```sh 
sudo apt install python3 python3-pip -y 
```

Verify the installation
```sh
python3 --version
pip3 --version
```

## Step 3: Set Up a Virtual Environment
Create a virtual environment for your project:
```sh
sudo apt install python3-venv -y
python3 -m venv venv
```

Activate the virtual environment
```sh
source venv/bin/activate
```

## Step 4: Install FastAPI and Uvicorn
```sh
pip install -r requirements.txt
```

## Step: Run FastAPI Server
```sh
fastapi run main.py --host [port] --port [port]
```

# -------------[ Setup Backend ]---------------
## Prerequisites
- apache2
- nodejs, pm2
- certbot

## Step 0 :
Pastikan sudah clone & setup backend

## Step 1 : Membuat Virtual Host
```sh 
cd /etc/apache2/sites-available
```

Enable modul untuk Proxy
```sh 
sudo a2enmod proxy proxy_ajp proxy_http rewrite deflate headers proxy_balancer proxy_connect proxy_html
```

Membuat Virtual host untuk backend
```sh 
sudo nano tts.conf
```

Paste text dibawah ini
```sh
<VirtualHost *:80>
    ServerName sub-domain.net
    ServerAlias sub-domain.net
    ServerAdmin webmaster@localhost

    ProxyPreserveHost On
    ProxyPass / http://0.0.0.0:[port dari backend di atas]/
    ProxyPassReverse / http://0.0.0.0:[port dari backend di atas]/

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
RewriteEngine on
RewriteCond %{SERVER_NAME} = sub-domain.net
SetEnv proxy-initial-not-pooled 1
    RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>
```

Save & Exit

## Step 2 : Membuat Sertifikat SSL
Akses user root
```sh
sudo su
```

Buat sertifikat SSL gratis dengan letsencrypt
```sh 
sudo certbot ---apache -d [sub-domain.net]
````

Pastikan sudah muncul file tts-le-ssl.conf di ```/etc/apache2/sites-available```
Jika belum, silahkan dibuat dan paste text ini.

```sh
<IfModule mod_ssl.c>
<VirtualHost *:443>
    ServerName [sub-domain.net]
    ServerAlias [sub-domain.net]
    ServerAdmin webmaster@localhost

    ProxyPreserveHost On
    ProxyPass / http://0.0.0.0:[port dari backend di atas]/
    ProxyPassReverse / http://0.0.0.0:[port dari backend di atas]/

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
RewriteEngine on
# Some rewrite rules in this file were disabled on your HTTPS site,
# because they have the potential to create redirection loops.

# RewriteCond %{SERVER_NAME} =[sub-domain.net]
# SetEnv proxy-initial-not-pooled 1
#     RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]

SSLCertificateFile /etc/letsencrypt/live/[sub-domain.net]/fullchain.pem
SSLCertificateKeyFile /etc/letsencrypt/live/[sub-domain.net]/privkey.pem
Include /etc/letsencrypt/options-ssl-apache.conf
</VirtualHost>
</IfModule>
```

Keluar dari user root
```sh 
exit
```

## Step 3 : Enable konfigurasi
Enable virtual host yang baru dibuat
```sh 
sudo a2ensite tts.conf
```

Enable SSL
```sh 
sudo a2ensite tts-le-ssl.conf
```

Restart apache
```sh 
sudo systemctl restart apache2
```

## Step 4 : Run Website
Pastikan process pm2 dari tahap setup backend masih online.

Akses website di [sub-domain.net]