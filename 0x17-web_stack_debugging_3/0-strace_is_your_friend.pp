# removes a typo to fix an apache server returning 500 error
$file_path = '/var/www/html/wp-settings.php'

exec { 'replace_text_in_file':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' ${file_path}",
  path    => '/bin:/usr/bin',
  onlyif  => "test -f ${file_path}",
}
