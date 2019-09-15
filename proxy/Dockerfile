FROM debian:9

MAINTAINER Kirill admin@vahra.ru

# install nginx
RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get install -y nginx

# replace nginx config file
COPY nginx.conf /etc/nginx/nginx.conf

# open port
EXPOSE 8080

# autostart nginx
ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;"]
