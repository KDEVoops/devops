FROM debian:9.11
MAINTAINER Kirill admin@vahra.ru

# install apache2
apt-get update
apt-install apache2 -y
service apache2 start

# copy index file to apache dir
cp index.php /var/www/html/index.php