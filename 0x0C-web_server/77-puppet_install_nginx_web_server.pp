# install and configare nginx server
# Nginx should be listening on port 80
# when requesting the root / a page with Hello World! will be returned
# The redirection must be a “301 Moved Permanently”

# declaring a class to orginize all files and configrations related to nginx

class nginx {

	# update the packages
	exec { 'update_linux_packages':
        command  => 'apt-get update',
	}
	
	# ensure the instalation of the nginx
	package { 'nginx':

        ensure   => installed,
		provider => 'apt'
	}

    # ensure the /var/www directory exists
    file { '/var/www':
        ensure => directory,
    }
    # ensure the /var/www/html directory exists
    file { '/var/www/html':
        ensure => directory,
    }
	# create the content for the main html page

	file { '/var/www/html/index.html':
        ensure  => file,
		content => 'Hello World!',
	}
	
	# create the content for the error_page
	
	file {'/var/www/html/page_not_found.html':
		ensure  => file,
		content => 'Ceci n\'est pas une page',
	}
	
	# use a templete for the /etc/sites-available/default 
	 file { '/etc/nginx/sites-available/default':
        ensure  => file,
        content => template('nginx_setup/default.erb'),
        notify  => Service['nginx'],
  	}

  	service { 'nginx':
    	ensure    => running,
    	enable    => true,
  	}
		
}
