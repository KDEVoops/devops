FROM debian:9

MAINTAINER Kirill admin@vahra.ru

# install lighttpd
RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get install -y lighttpd

# Del defaults
#RUN rm -f /var/www/html/index.lighttpd.html
# copy index file to web dir
COPY index.html /var/www/html/index.html
COPY lighttpd.conf /etc/lighttpd/lighttpd.conf
# open port
EXPOSE 80

# autostart lighttpd
ENTRYPOINT ["/usr/sbin/lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]


