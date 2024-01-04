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
  content => template('nginx_setup/default.erb'),
}

# Ensure the Nginx service is running
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

