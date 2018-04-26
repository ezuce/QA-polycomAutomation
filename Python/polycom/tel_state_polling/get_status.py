#!/usr/bin/env python
#
#
# curl --digest -k -X GET https://Test:Test@10.1.0.14/polling/callstateHandler
#
# TODO: add parameter ip of phone

import requests
import sys
from xml.etree import ElementTree

from requests.auth import HTTPDigestAuth

user = "Test"
pwd = "Test"
phone_ip = '10.1.0.14'


api_url='https://{}/polling/callstateHandler' .format(phone_ip)

response = requests.get(api_url, verify=False, auth=HTTPDigestAuth(user, pwd))
resp_xml = response.text

print resp_xml
print "-----------------------------------------------\n"


root = ElementTree.fromstring(resp_xml)




