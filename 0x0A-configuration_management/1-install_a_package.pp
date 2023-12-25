# Using Puppet, install flask from pip3.

# Requirements:

# Install flask
# Version must be 2.1.0

package {
    'python3':
    ensure  => '3.8.10',
}

package {
    'python3-pip':
    ensure  => installed,
    require => Package['python3'],
}

package {
    'flask':
    ensure   => '2.1.0',
    require  => Package['python3', 'python3-pip'],
    provider => 'pip3',
}

package {
    'Werkzeug':
    ensure   => '2.1.0',
    require  => Package['python3', 'python3-pip', 'flask'],
    provider => 'pip3',
}

