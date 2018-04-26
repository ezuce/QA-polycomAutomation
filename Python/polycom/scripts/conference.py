#!/usr/bin/env python
#
# Call number 202 and 203 from 10.1.0.14 with HTTPS curl
# Get the phone status for the two numbers, then join the two numbers to a conference
#

import requests
import sys
import time
import xml.etree.ElementTree as ET

from requests.auth import HTTPDigestAuth

from requests.packages.urllib3.exceptions import InsecureRequestWarning		#ignore warnings - not recommended
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

user = "Test"
pwd = "Test"
phone_ip = '10.1.0.14'
phone_no_1 = '202'
phone_no_2 = '203'

api_url = 'https://{}/push' .format(phone_ip)
s_headers = {'Content-Type': 'application/x-com-polycom-spipx'}
s_data_c1 = ' <PolycomIPPhone><Data priority="Critical">tel:\\{};line1</Data></PolycomIPPhone> ' .format(phone_no_1)
s_data_c2 = ' <PolycomIPPhone><Data priority="Critical">tel:\\{};line2</Data></PolycomIPPhone> ' .format(phone_no_2)

response_c1 = requests.post(api_url, verify=False, auth=HTTPDigestAuth(user, pwd), headers=s_headers, data=s_data_c1 )


# Checking for status change and connecting first call

api_url='https://{}/polling/callstateHandler' .format(phone_ip)

linestate = "Inactive"
callstate = "None"

while (linestate == "Inactive"):													# keep polling line state
	response = requests.get(api_url, verify=False, auth=HTTPDigestAuth(user, pwd))
	resp_xml = response.text

	xmls = ET.fromstring(resp_xml)
	ls = xmls.find('CallLineInfo/LineState')
	linestate = ls.text
	print linestate
	time.sleep(0.5)

while (callstate != "Connected"):													# keep polling connection status
	response = requests.get(api_url, verify=False, auth=HTTPDigestAuth(user, pwd))
	resp_xml = response.text

	xmls = ET.fromstring(resp_xml)
	cs = xmls.find('CallLineInfo/CallInfo/CallState')
	callstate = cs.text

	cref = xmls.find('CallLineInfo/CallInfo/CallReference')			# loops over child elements of the values element
	callRef = cref.text

	print callstate
	time.sleep(0.5)

time.sleep(2)

# try to set up a conference

print "Callref is: " + cref.text
s_data_conf = ' <PolycomIPPhone><Data priority="Critical">CallAction:Conference;nCallReference={}</Data></PolycomIPPhone> ' .format(cref.text)	# error 405 method not allowed?!
response = requests.post(api_url, verify=False, auth=HTTPDigestAuth(user, pwd), headers=s_headers, data=s_data_conf )

response_c2 = requests.post(api_url, verify=False, auth=HTTPDigestAuth(user, pwd), headers=s_headers, data=s_data_c2 )

# more difficult with second line. To implement

# call c1, get status. While status is not connected, keep waiting. Answer call. Save status details
# call c2, get status. While status is not connected, keep waiting. Answer call. Save status details
# join the two calls



if (response.status_code == requests.codes.ok):
	print response.text
else:
	print 'Error! Status code: {}' .format(response.status_code)


# call number 1 -> wait until call becomes active -> call number 2 -> wait until call again becomes active.
