# change the configration file
include stdlib

file_line {
    'IdentityFile':
    path  => /etc/ssh/ssh_config,
    line  => 'IdentityFile ~/.ssh/school',
    match => '^IdentityFile',
}

file_line {
    'PasswordAuthentication':
    path  => /etc/ssh/ssh_config,
    line  => 'PasswordAuthentication no',
    match => '^PasswordAuthentication',
}
