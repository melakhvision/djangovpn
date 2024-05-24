#!/bin/bash

CLIENT=$1
export CLIENT=$CLIENT
echo $CLIENT
cd /root && AUTO_INSTALL=y PASS=1 CLIENT=$CLIENT ./openvpn.sh

## COPY PORFILE TO MEDIA TO MAKE IT ACCESSIBLE
cp /root/$CLIENT.ovpn /var/www/html/media/$CLIENT.ovpn

## RESET CLIENT TO NULL
export CLIENT=
