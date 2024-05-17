## Create a core project in the current directory

```bash
django-admin startproject core .
```

## Create app named vpn

```bash
python manage.py startapp vpn
```
## Install packages

```bash
sudo apt update
sudo apt install jq netcat
```
### Enable Management
1. edit server.conf in /etc/openvpn/server.conf and ad this line
```bash
management localhost 7505
```
2. Restart the server

```bash
sudo systemctl restart openvpn@server
```

3. Check the status.

```bash
telnet localhost 7505
status
```
