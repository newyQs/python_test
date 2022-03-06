1. fatal error: Python.h: No such file or directory
```text
For apt (Ubuntu, Debian...):

sudo apt-get install python-dev   # for python2.x installs
sudo apt-get install python3-dev  # for python3.x installs
For yum (CentOS, RHEL...):

sudo yum install python-devel    # for python2.x installs
sudo yum install python3-devel   # for python3.x installs
For dnf (Fedora...):

sudo dnf install python2-devel  # for python2.x installs
sudo dnf install python3-devel  # for python3.x installs
For zypper (openSUSE...):

sudo zypper in python-devel   # for python2.x installs
sudo zypper in python3-devel  # for python3.x installs
For apk (Alpine...):

# This is a departure from the normal Alpine naming
# scheme, which uses py2- and py3- prefixes
sudo apk add python2-dev  # for python2.x installs
sudo apk add python3-dev  # for python3.x installs
For apt-cyg (Cygwin...):

apt-cyg install python-devel   # for python2.x installs
apt-cyg install python3-devel  # for python3.x installs
```