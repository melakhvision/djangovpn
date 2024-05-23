#!/bin/bash
## remove a certificate and ovpn profile
CLIENT=$0

cd /etc/openvpn/easy-rsa/ || return
./easyrsa --batch revoke "$CLIENT"
EASYRSA_CRL_DAYS=3650 ./easyrsa gen-crl
rm -f /etc/openvpn/crl.pem
cp /etc/openvpn/easy-rsa/pki/crl.pem /etc/openvpn/crl.pem
chmod 644 /etc/openvpn/crl.pem
find /home/ -maxdepth 2 -name "$CLIENT.ovpn" -delete
rm -f "/root/$CLIENT.ovpn"
sed -i "/^$CLIENT,.*/d" /etc/openvpn/ipp.txt
rm -rf "/var/www/html/media/$CLIENT.ovpn"
cp /etc/openvpn/easy-rsa/pki/index.txt{,.bk}

echo ""
echo "Certificate for client $CLIENT revoked."
