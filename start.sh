#!/bin/bash

# Replace 'yourscript.py' with the path to your script
# check if all .sh file in the script folder has the execute permission
# if not, add the execute permission
# if yes, start the Django server
for file in /var/www/html/vpn/script/*.sh; do
    if [ ! -x "$file" ]; then
        chmod +x "$file"
    fi
done

# Start the Django server
#python3 manage.py runserver
daphne -t 60 --application-close-timeout 60 core.asgi:application
