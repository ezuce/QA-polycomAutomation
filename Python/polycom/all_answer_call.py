#!/usr/bin/env python
#
#	This script answers an incoming call
#
#	# 	Get status: 
# curl --digest -k -X GET https://Test:Test@10.1.0.14/polling/callstateHandler
#
# 	Answer call: 
# curl --digest -u Test:Test -d $'<PolycomIPPhone><Data priority="Critical">CallAction:Answer;nCallReference=0x411cbc80</Data></PolycomIPPhone>' --header "Content-Type: application/x-com-polycom-spipx" https://10.1.0.14/push
#
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
phone_ip = '10.1.0.12'		# vvx500



# Getting status from phone_ip_2

api_url='https://{}/polling/callstateHandler' .format(phone_ip)

response = requests.get(api_url, verify=False, auth=HTTPDigestAuth(user, pwd))
resp_xml = response.text

print resp_xml
print "-----------------------------------------------\n"

xmls = ET.fromstring(resp_xml)

values = xmls.find('CallLineInfo/CallInfo/CallReference')			# loops over child elements of the values element
callRef = values.text
print values.text



# Answering call from phone_ip_2 (line 202)

api_url = 'https://{}/push' .format(phone_ip)
s_headers = {'Content-Type': 'application/x-com-polycom-spipx'}
s_data = ' <PolycomIPPhone><Data priority="Critical">CallAction:Answer;nCallReference={}</Data></PolycomIPPhone> ' .format(values.text)

response = requests.post(api_url, verify=False, auth=HTTPDigestAuth(user, pwd), headers=s_headers, data=s_data )

if (response.status_code == requests.codes.ok):
	print response.text
else:
	print 'Error! Status code: {}' .format(response.status_code)
	exit()



