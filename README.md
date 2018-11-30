# InstallUpdateNagios
Python script to install Nagios on Debian 9

## Prepare your setup

To use this script you need to install Python3 and pip3.
* On debian/ubuntu : `apt install python3`
* On centos : `yum install python3`
* On Windows : install the last 3.X version on : https://www.python.org/downloads/

In the installation, be carrefull to select the option `Add Python to environnment variables`

![Python_Install](https://i.imgur.com/TMMV3nE.png)

When that was done, you have to edit the script `variables.py` with your own informations.

## Run the script

`python3 install.py`
`python3 update.py`

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
