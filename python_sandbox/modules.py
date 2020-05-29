# A file containing a set of functions

# import datetime
from datetime import date
from time import time

# Pip module
from camelcase import CamelCase

c = CamelCase()
print(c.hump("hello there"))

# today = datetime.date.today()
today = date.today()
timestamp = time()

# pip3 install camelcase

# pip3 freeze
"""
appdirs==1.4.4
apturl==0.5.2
...
six==1.11.0
system-service==0.3
systemd-python==234
toml==0.10.1
typed-ast==1.4.1
ubuntu-drivers-common==0.0.0
ufw==0.36
unattended-upgrades==0.1
urllib3==1.22
wadllib==1.3.2
xkit==0.0.0
zope.interface==4.3.2
"""

print(today, timestamp)

# import custom module
from validator import validate_email

email = "teste@yahoo.com"
wrong_email = "vinicius@com"

if validate_email(wrong_email):
    print("Valid Email")
else:
    print("Invalid email")
