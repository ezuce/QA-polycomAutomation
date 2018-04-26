#!/usr/bin/env python
#
#

import requests
import sys

from requests.auth import HTTPDigestAuth

user = "201"
pwd = "12345678"

if len(sys.argv) != 2:								# exit if format not correct
	print 'Usage: {} <entry name>' .format(sys.argv[0])
	sys.exit(2)

entry = sys.argv[1]
api_url='https://10.1.0.111/sipxconfig/rest/my/phonebook/entry' .format(entry)

response = requests.get(api_url, verify=False, auth=HTTPDigestAuth(user, pwd))

if (response.status_code == requests.codes.ok):
	print response.text
else:
	print 'Error! Status code: {}' .format(response.status_code)


