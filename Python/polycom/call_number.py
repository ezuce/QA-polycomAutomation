#!/usr/bin/env python
#
# Call number 202 from 10.1.0.14 with HTTPS curl
# curl --digest -u Test:Test -d  "<PolycomIPPhone><Data priority='"Critical"'>tel:\\202</Data></PolycomIPPhone>" --header "Content-Type: application/x-com-polycom-spipx" https://10.1.0.14/push -k
# TODO: add parameters ip and line to call


import requests
import sys

from requests.auth import HTTPDigestAuth

user = "Test"
pwd = "Test"
phone_ip = '10.1.0.14'
phone_no = '202'

api_url = 'https://{}/push' .format(phone_ip)
s_headers = {'Content-Type': 'application/x-com-polycom-spipx'}
s_data = ' <PolycomIPPhone><Data priority="Critical">tel:\\{}</Data></PolycomIPPhone> ' .format(phone_no)

response = requests.post(api_url, verify=False, auth=HTTPDigestAuth(user, pwd), headers=s_headers, data=s_data )

if (response.status_code == requests.codes.ok):
	print response.text
else:
	print 'Error! Status code: {}' .format(response.status_code)
