#!/usr/bin/env bash
#  script that sets up your web servers for the deployment of web_static

#first update the machine
echo "updating the system..."
sudo apt-get update

if command -v nginx
then
	echo "Nginx is already installed"
else
	sudo apt-get install -y nginx &> /dev/null
fi

# check if the /data/web_static exits else create it
if [ ! -d "/data/web_static/" ]
then
	echo "creating new directory: /data/web_static.."
	sudo mkdir -p "/data/web_static"
else
	echo "Directory /data/web_static/ already exists.."
fi

# create /data/web_static/releases/ directory if it doesnt exist
if [ ! -d "/data/web_static/releases/" ]
then
	echo "creating new directory: /data/web_static/releases/.."
	sudo mkdir -p "/data/web_static/releases/"
else
	echo "Directory /data/web_static/releases/ already exists.."
fi

# create /data/web_static/shared/ if it doest not exits
if [ ! -d "/data/web_static/shared/" ]
then
	echo "Creating new directory: /data/web_static/shared/.."
	sudo mkdir -p "/data/web_static/shared/"
else
	echo "Directory /data/web_static/shared/\" already exits.."
fi

# create /data/web_static/releases/test/ if it does not exits
if [ ! -d "/data/web_static/releases/test/" ]
then
	echo "Creating new directory /data/web_static/releases/test/.."
	sudo mkdir -p "/data/web_static/releases/test/"
else
	echo "Directory already exits"
fi

# Create a fake HTML file /data/web_static/releases/test/index.html
# (with simple content, to test your Nginx configuration)
sudo mkdir -p "/data/web_static/releases/test/index.html"

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" >> /data/web_static/releases/test/index.html

# path in which the synbolic link is pointing to:
path_pointedToByLink="/data/web_static/releases/test/"

# container to hose the link
symbolic_link="/data/web_static/current"

# check if the synbolic link exits and delete it if it does
if [ -L "$symbolic_link" ]
then
	echo "Deleteing the existing symbolic link..."
	sudo rm "$symbolic_link"
fi

# Create new sybolic link each time the program is ran
echo "Creating a new symbolic link"
sudo ln -s "$symbolic_link" "$path_pointedToByLink"

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# update Ngnix config. to serve /data/web_static/current/ to  hbnb_static
sudo sed -i "26i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

# retstart Ngnix
sudo service nginx restart
