FROM debian:9

MAINTAINER Kirill admin@vahra.ru

# install apache2
RUN apt-get update
RUN apt-get install apt-utils -y
RUN apt-get install apache2 -y

CMD service apache2 start

# copy index file to apache dir
COPY /home/adminko/docker/devops/apache/index.php /var/www/html/index.php

# open port
EXPOSE 80
