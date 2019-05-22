#!/usr/bin/env bash

sudo aptitude update -y
sudo aptitude upgrade -y
sudo apt-get autoremove

sudo aptitude -y install python-pip
sudo aptitude install -y build-essential git mercurial subversion
sudo aptitude install -y libfreetype6 libfreetype6-dev libjpeg62 libjpeg62-dev libxml2-dev libxslt1-dev lynx openssl xpdf wv
sudo aptitude install -y python-dev python-mysqldb libmysqlclient-dev virtualenvwrapper ntp
sudo aptitude install -y redis-server nginx rabbitmq-server
sudo aptitude install -y supervisor

sudo ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib/
sudo ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib/
sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib/

sudo pip install virtualenv
sudo timedatectl set-timezone America/Los_Angeles

sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
sudo sh -c 'echo "/swapfile none swap sw 0 0" >> /etc/fstab'

echo "export WORKON_HOME=~/.virtualenvs" >> ~/.bashrc
echo "source /usr/share/virtualenvwrapper/virtualenvwrapper.sh" >> ~/.bashrc
source ~/.bashrc

sudo debconf-set-selections <<< "postfix postfix/mailname string brentrojas.com"
sudo debconf-set-selections <<< "postfix postfix/main_mailer_type string 'Internet Site'"
sudo aptitude install postfix -y

sudo sed -i 's/port 6379/#port 6379/' /etc/redis/redis.conf
sudo sed -i 's/bind 127.0.0.1/#bind 127.0.0.1/' /etc/redis/redis.conf
sudo sed -i 's|# unixsocket /var/run/redis/redis.sock|unixsocket /var/run/redis/redis.sock|' /etc/redis/redis.conf
sudo sed -i 's/# unixsocketperm 755/unixsocketperm 777/' /etc/redis/redis.conf
sudo service redis-server restart

cd /usr/local/bin/
sudo wget -O p4 https://s3.amazonaws.com/KestrelCodeworks/Resources/P4-LINUX26X86_64-2012.2-538478
sudo chmod 755 p4

#sudo aptitude install -y openjdk-7-jre
#wget https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.7.2.deb
#sudo dpkg -i elasticsearch-1.7.2.deb
#sudo update-rc.d elasticsearch defaults

