#!/bin/sh

# Start Gunicorn in the background
python3 -m gunicorn --workers=2 --bind 0.0.0.0:8000 --timeout 60 core.wsgi &

# Check if Gunicorn is available
while ! curl -s http://localhost:8000/ >/dev/null; do
    echo "Waiting for Gunicorn to be available..."
    sleep 1
done

# Start Nginx
nginx -g "daemon off;"
