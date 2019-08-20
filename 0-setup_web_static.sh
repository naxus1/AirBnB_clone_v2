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
    sudo mkdir $file
fi
file="/data/web_static/"
if [ -e $file ]
then
    true
else
    sudo mkdir $file
fi
file="/data/web_static/releases/"
if [ -e $file ]
then
    true
else
    sudo mkdir $file
fi
file2="/data/web_static/shared/"
if [ -e $file2 ]
then
    true
else
    sudo mkdir $file2
fi
file="/data/web_static/releases/test/"
if [ -e $file ]
then
    true
else
    sudo mkdir $file
fi
sudo echo -e "<html>\n\t<body>\n\t<h1>Esto es una prueba</h1>\n\t</body>\n</html>" | sudo tee -a /data/web_static/releases/test/index.html
file_current=/data/web_static/current
if [ -e $file_current ]
then
    sudo rm $file_current
fi
sudo ln -s $file $file_current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "56i\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default
sudo service nginx restart
