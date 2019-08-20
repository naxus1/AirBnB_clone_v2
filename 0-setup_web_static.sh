#!/usr/bin/env bash
# configure server
file="/etc/nginx"
if [ -e $file ]
then
    true
else
    sudo apt update
    sudo apt -y install nginx
    sudo ufw allow 'Nginx HTTP'
fi
file="/data/"
if [ -e $file ]
then
    true
else
    mkdir $file
fi
file="/data/web_static/"
if [ -e $file ]
then
    true
else
    mkdir $file
fi
file="/data/web_static/releases/"
if [ -e $file ]
then
    true
else
    mkdir $file
fi
file2="/data/web_static/shared/"
if [ -e $file2 ]
then
    true
else
    mkdir $file2
fi
file="/data/web_static/releases/test/"
if [ -e $file ]
then
    true
else
    mkdir $file
fi
echo -e "<html>\n\t<body>\n\t<h1>Esto es una prueba</h1>\n\t</body>\n</html>" > /data/web_static/releases/test/index.html
file_current=/data/web_static/current
if [ -e $file_current ]
then
    rm $file_current
    ln -s $file $file_current
else
    ln -s $file $file_current
fi
chown -R ubuntu:ubuntu /data/
sed -i "56i\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default
service nginx restart
