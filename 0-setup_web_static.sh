#!/usr/bin/env bash
# Script that sets up  web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
filename=/data/web_static/releases/test/index.html
sudo touch $filename
content=\
"<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
  </html>
"
echo -n "$content" > "$filename"
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
printf %s "server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root   /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	server_name _
	add_header X-Served-By $HOSTNAME;

	location / {
		try_files \$uri \$uri/ =404;
	}
	
	location /hbnb_static {
		alias /data/web_static/current;
		index index.html index.htm;
	}

	error_page 404 /custom_404.html;
	location /custom_404.html {
		root /var/www/error;
		internal;
	}
	
	location /redirect_me/ {
		rewrite ^(.*)$ http://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
	}
}" > /etc/nginx/sites-enabled/default
sudo service nginx restart
