"""

Functions used in install.py and update.py

"""

import os

from variables import *

def install_nagios():
	"""  """

	os.system("apt install build-essential libgd2-xpm-dev openssl libssl-dev xinetd apache2-utils apache2 unzip php -y")

	os.system("mkdir /home/nagios")
	os.system("chown nagios:nagios /home/nagios")
	os.system("groupadd nagcmd")
	os.system("usermod -a -G nagcmd nagios")

	os.system("cd /opt/")
	os.system("wget https://assets.nagios.com/downloads/nagioscore/releases/nagios-{}.tar.gz".format(NAGIOS_VERSION))
	os.system("tar xzvf nagios-{}.tar.gz".format(NAGIOS_VERSION))

	os.system("cd /opt/nagios-{}".format(NAGIOS_VERSION))
	os.system("./configure --with-nagios-group=nagcmd --with-command-group=nagcmd --with-httpd-conf=/etc/apache2/conf-available")
	os.system("make all")
	os.system("make install")
	os.system("make install-commandmode")
	os.system("make install-init")
	os.system("make install-config")
	os.system("/usr/bin/install -c -m 644 sample-config/httpd.conf /etc/apache2/sites-available/nagios.conf")
	os.system("usermod -G nagcmd www-data")
	os.system("ln -s /etc/init.d/nagios /etc/rcS.d/S99nagios")


def install_plugins():
	"""  """

	os.system("cd /opt/")
	os.system("wget http://www.nagios-plugins.org/download/nagios-plugins-{}.tar.gz".formart(PLUGINS_VERSION))
	os.system("tar xvf nagios-plugins-{}.tar.gz".formart(PLUGINS_VERSION))
	os.system("cd /opt/nagios-plugins-{}/ && ./configure --with-nagios-user=nagios --with-nagios-group=nagcmd".formart(PLUGINS_VERSION))
	os.system("cd /opt/nagios-plugins-{}/ && make".formart(PLUGINS_VERSION))
	os.system("cd /opt/nagios-plugins-{}/ && make install".formart(PLUGINS_VERSION))


def conf_apache():
	"""  """

	os.system("a2enmod rewrite")
	os.system("a2enmod cgi")

	os.system("htpasswd -c /usr/local/nagios/etc/htpasswd.users nagiosadmin")

	os.system("a2ensite nagios")

	os.system("systemctl start nagios.service ")
	os.system("systemctl reload apache2.service")


def update_nagios():
	""" """

	os.system("su -l nagios")
	os.system("cd /tmp")
	os.system("wget https://assets.nagios.com/downloads/nagioscore/releases/nagios-4.2.0.tar.gz".format(NAGIOS_VERSION))
	os.system("tar xzvf nagios-{}.tar.gz".format(NAGIOS_VERSION))
	os.system("cd nagios-{}/".format(NAGIOS_VERSION))
	os.system("./configure --with-command-group=nagios")   
	os.system("make all")
	os.system("make install")
	os.system("service nagios restart")