# fixes to allow the holberton user to login and open files without error

exec { 'increasing the hard and soft file limit':
  provider => shell,
  command  => 'sed -i "/holberton hard/s/5/50000/" \
                /etc/security/limits.conf; \
                sed -i "/holberton soft/s/4/50000/" \
                /etc/security/limits.conf',
}
