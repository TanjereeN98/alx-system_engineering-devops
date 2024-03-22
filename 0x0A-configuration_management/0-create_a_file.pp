# Requirements: File path is /tmp/school, File permission is 0744, File owner is www-data
file { '/tmp/school':
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet'
}
