FROM debian:9

MAINTAINER Kirill admin@vahra.ru

# install apache2
RUN apt-get update
RUN apt-get install apt-utils -y
RUN apt-get install apache2 -y
RUN apt-get install php7.0 -y

RUN rm -f /var/www/html/index.html
RUN rm -f /var/www/html/index.html
# copy index file to apache dir
COPY index.php /var/www/html/index.php

# open port
EXPOSE 80

# autostart apache2
ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
