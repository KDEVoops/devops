FROM debian:9

MAINTAINER Kirill admin@vahra.ru

# install packages
RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get install -y apache2 
RUN apt-get install -y libapache2-mod-wsgi python-dev
RUN apt-get install -y python3
RUN apt-get install -y python3-venv
RUN apt-get install -y python3-pip
RUN a2enmod wsgi
RUN pip3 install flask

# app dir
RUN mkdir /var/www/verapp

# evnvirments for app
RUN export LANG=C.UTF-8
RUN export LC_ALL=C.UTF-8
RUN export FLASK_APP=verapp.py


#copy flask app
COPY flask.py /var/www/verapp/verapp.py
# open port
EXPOSE 80

# autostart apache2
ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
