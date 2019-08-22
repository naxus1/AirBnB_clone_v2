# deployment
exec {'update':
  command => '/usr/bin/apt-get update',
}
-> package {'nginx':
  ensure => 'present',
}
-> exec {'folders':
  command => 'mkdir -p /data/web_static/shared/ /data/web_static/releases/test/',
  path => '/usr/bin:/usr/sbin:/bin',
}
-> exec {'dummy page':
  command => 'echo "fake content" | sudo tee /data/web_static/releases/test/index.html',
  path => '/usr/bin:/usr/sbin:/bin',
}
-> exec {'sym link':
  command =>'ln -nsf /data/web_static/releases/test/ /data/web_static/current',
  path => '/usr/bin:/usr/sbin:/bin',
}
-> exec {'ownership':
  command => 'chown ubuntu:ubuntu -R /data/',
  path => '/usr/bin:/usr/sbin:/bin',
}
-> exec {'conf nginx':
  command => 'sed -i \'72i\\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}\' /etc/nginx/sites-enabled/default',
  path => '/usr/bin:/usr/sbin:/bin',
}
-> exec {'run2':
  command => '/usr/sbin/service nginx restart',
}