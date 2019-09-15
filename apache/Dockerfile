FROM debian:9

MAINTAINER Kirill admin@vahra.ru

# install apache2
RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get install -y apache2 
RUN apt-get install -y php7.0

# copy index file to apache dir
RUN rm -f /var/www/html/index.html
COPY index.php /var/www/html/index.php
COPY httpd.conf /etc/apache2/apache2.conf

# open port
EXPOSE 80

# autostart apache2
ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
