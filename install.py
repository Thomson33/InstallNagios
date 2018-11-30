"""

Install nagios and his plugins

"""

from variables import *

plug = input("o/n")


install_nagios()

if plug == "o":
	install_plugins()

conf_apache()