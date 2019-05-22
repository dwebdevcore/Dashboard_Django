sudo -i -u olivino export P4PORT=perforce.kestrelcodeworks.com:1666
sudo -i -u olivino p4 -c DJANGO-EXPORT -p perforce.kestrelcodeworks.com:1666 -u export -P 76Eldorado sync /opt/django/olivino/...#head
#sudo chown -R olivino /opt/django/olivino


