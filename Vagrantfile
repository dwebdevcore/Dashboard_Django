# -*- mode: ruby -*-
# vi: set ft=ruby :

API_VERSION = "2"

# BOX = "box-name"
BOX = "ubuntu/trusty64"

# HOSTNAME = "machine-name"
HOSTNAME = "olivino-dev"

# You can use the following IP ranges:
#   10.0.0.1    - 10.255.255.254
#   172.16.0.1  - 172.31.255.254
#   192.168.0.1 - 192.168.255.254
IP = "192.168.22.75"

Vagrant.configure(API_VERSION) do |config|

  config.vm.box = BOX

   config.vm.network "private_network", ip: IP

    config.vm.provider :virtualbox do |vb|
       vb.name = HOSTNAME
    end

   config.vm.provision :shell, path: "bin/server_setup.sh"
end
