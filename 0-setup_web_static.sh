#!/usr/bin/env bash
# Script to set up web servers for web_static deployment

# Update system and install Nginx if not already installed
echo "Updating system and installing Nginx..."
sudo apt-get update
sudo apt-get install -y nginx

# Create necessary directories if they don't exist
echo "Creating directories..."
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create a test HTML file for deployment
echo "Creating test HTML file..."
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" >> /data/web_static/releases/test/index.html

# Create or recreate a symbolic link
echo "Creating symbolic link..."
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the directories to ubuntu user and group
echo "Assigning ownership..."
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve /data/web_static/current at /hbnb_static/
echo "Updating Nginx configuration..."
sudo sed -i "26i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

# Restart Nginx to apply changes
echo "Restarting Nginx..."
sudo service nginx restart

echo "Setup complete!"
