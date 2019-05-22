#!/usr/bin/env bash

sudo chown -R olivino:webapps /opt/django/olivino
#loggin with user
sudo su - olivino
# install new dependences
source venv/bin/activate
/opt/django/olivino/venv/bin/pip install -r /opt/django/olivino/requirements.txt
# collect new static files
echo yes | /opt/django/olivino/venv/bin/python /opt/django/olivino/manage.py collectstatic --c
# collect new static files for production
echo yes | /opt/django/olivino/venv/bin/python /opt/django/olivino/manage.py collectstatic --c --settings=olivino.settings.production
# migrate bd changes
/opt/django/olivino/venv/bin/python /opt/django/olivino/manage.py migrate
