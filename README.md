# devops
REQUIREMENTS
============
For name resolving without DNS-server (until I add dnsmasq) add a line to /etc/hosts file using command:
<p><i>echo '127.0.0.1 apache flask lighttpd' >> /etc/hosts</i></p>


TESTED ON
=====================
Docker Engine - Community Version: 19.03.2
<p>docker-compose version 1.8.0</p>



KNOWN ISSUES
=====================
<ul>
  <li>DNS resolver for accessing web servers in containers by name without hosts file.</li>
  <li>Flask app</li>
</ul>
