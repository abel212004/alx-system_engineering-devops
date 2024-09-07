# fixes to allow the nginx server to handle more traffic

exec { 'fixing and restarting nginx':
  provider => shell,
  command  => 'sed -i "s/15/4096/" /etc/default/nginx; \
                sudo service nginx restart',
}
