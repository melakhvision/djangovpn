FROM python:3.10-alpine
RUN mkdir store
WORKDIR /ovpn

RUN apk update \
    && apk add curl nginx \
    && apk add --virtual build-deps gcc python3-dev musl-dev   \
    && pip3 install gunicorn \
    && apk add --no-cache mariadb-dev mariadb-client python3-dev build-base \
    && apk del build-deps 

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN 
COPY . .
RUN python3 manage.py collectstatic --noinput
COPY nginx.conf /etc/nginx/nginx.conf
RUN rm -rf .env
COPY start.sh /start.sh
EXPOSE 8000 80
RUN chmod 755 /start.sh
CMD ["sh", "/start.sh" ]