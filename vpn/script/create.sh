#!/bin/bash

CLIENT=$0
export CLIENT=$CLIENT

AUTO_INSTALL=y PASS=1 CLIENT=$CLIENT ./roo/openvpn-install.sh

## COPY PORFILE TO MEDIA TO MAKE IT ACCESSIBLE
cp -r /root/$CLIENT.ovpn /var/www/html/media/$CLIENT.ovpn

## RESET CLIENT TO NULL
export CLIENT=
