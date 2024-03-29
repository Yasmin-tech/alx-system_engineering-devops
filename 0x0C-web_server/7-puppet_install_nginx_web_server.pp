# Update the system's packages
exec { 'update':
  command => 'apt-get -y update',
  path    => ['/bin', '/usr/bin'],
}

# Install the nginx package
package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

# Ensure the /var/www/html directory exists
file { '/var/www/html':
  ensure => directory,
}

# Create the main HTML page
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

# Create the Nginx server configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name _;

    location / {
        root /var/www/html;
        index index.html;
        if (\$request_uri ~ redirect_me){
            rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
        }
    }
}",
}

# Ensure the Nginx service is running
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

