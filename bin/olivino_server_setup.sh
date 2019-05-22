#######################
# instance specific

sudo groupadd --system webapps
sudo useradd --system --gid webapps --shell /bin/bash --home /opt/django/olivino olivino

#sudo mkdir -p /opt/django/olivino
sudo mkdir -p /opt/django/olivino/logs/
sudo touch /opt/django/olivino/logs/gunicorn_supervisor.log
sudo chown -R olivino /opt/django/olivino

sudo su - olivino
cd /opt/django/olivino

export P4PORT=perforce.kestrelcodeworks.com:1666
p4 -c DJANGO-EXPORT -p perforce.kestrelcodeworks.com:1666 -u export -P 76Eldorado sync -f /opt/django/olivino/...#head


virtualenv venv
venv/bin/pip install -r requirements.txt

chmod 755 bin/*.sh
exit #leave olivino and go back to vagrant user

sudo ln -s conf/supervisor.conf /etc/supervisor/conf.d/olivino.conf
sudo supervisorctl reread
sudo supervisorctl update

sudo ln -s /opt/django/olivino/nginx.conf /etc/nginx/sites-enabled/olivino

sudo service nginx restart