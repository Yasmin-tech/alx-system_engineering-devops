# Update the system's packages
exec { 'update':
  command  => 'sudo apt-get -y update',
  provider => shell,
  before   => Exec['install Nginx'],
}

# Install the nginx package
exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['add_header'],
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
exec { 'add_header':
  provider    => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "s/index index.html;/\
  index index.html;\n\tadd_header X-Served-By \"$HOST\";/"\
  /etc/nginx/sites-available/default',
  before      => Exec['restart Nginx'],
}

# Ensure the Nginx service is running
exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
