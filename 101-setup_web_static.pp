# Update apt packages
exec { 'apt-get-update':
  command => '/usr/bin/env apt-get -y update',
}

# Install Nginx
-> exec {'install-nginx':
  command => '/usr/bin/env apt-get -y install nginx',
}

# Create directories for static content
-> exec {'create-release-directory':
  command => '/usr/bin/env mkdir -p /data/web_static/releases/test/',
}
-> exec {'create-shared-directory':
  command => '/usr/bin/env mkdir -p /data/web_static/shared/',
}

# Create index.html for the static content
-> exec {'create-index-html':
  command => '/usr/bin/env echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html',
}

# Create a symbolic link to make 'test' the current release
-> exec {'create-symbolic-link':
  command => '/usr/bin/env ln -sf /data/web_static/releases/test /data/web_static/current',
}

# Configure Nginx to serve the static content
-> exec {'configure-nginx':
  command => '/usr/bin/env sed -i "/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
}

# Set ownership of directories to 'ubuntu'
-> exec {'set-directory-ownership':
  command => '/usr/bin/env chown -R ubuntu:ubuntu /data',
}

# Restart Nginx for changes to take effect
-> exec {'restart-nginx':
  command => '/usr/bin/env service nginx restart',
}
