#!/usr/bin/env python
#
#	The script will use the commands below to:
#	1. Place call from vvx600 to vvx500
#	2. Get the status from vvx500
#	3. Answer the call from vvx500
#
# 	Place call: 
# curl --digest -u Test:Test -d  "<PolycomIPPhone><Data priority='"Critical"'>tel:\\202</Data></PolycomIPPhone>" --header "Content-Type: application/x-com-polycom-spipx" https://10.1.0.14/push -k
# 
# 	Get status: 
# curl --digest -k -X GET https://Test:Test@10.1.0.14/polling/callstateHandler
#
# 	Answer call: 
# curl --digest -u Test:Test -d $'<PolycomIPPhone><Data priority="Critical">CallAction:Answer;nCallReference=0x411cbc80</Data></PolycomIPPhone>' --header "Content-Type: application/x-com-polycom-spipx" https://10.1.0.14/push
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
phone_ip_1 = '10.1.0.14'		# vvx600
phone_ip_2 = '10.1.0.12'		# vvx500

phone_no = 202					# phone number of vvx500



# Calling line 202 from phone_ip_1

api_url = 'https://{}/push' .format(phone_ip_1)
s_headers = {'Content-Type': 'application/x-com-polycom-spipx'}
s_data = ' <PolycomIPPhone><Data priority="Critical">tel:\\{}</Data></PolycomIPPhone> ' .format(phone_no)

response = requests.post(api_url, verify=False, auth=HTTPDigestAuth(user, pwd), headers=s_headers, data=s_data )

if (response.status_code == requests.codes.ok):
	print response.text
else:
	print 'Error! Status code: {}' .format(response.status_code)
	exit()



time.sleep(1)
# Getting status from phone_ip_2

api_url='https://{}/polling/callstateHandler' .format(phone_ip_2)

response = requests.get(api_url, verify=False, auth=HTTPDigestAuth(user, pwd))
resp_xml = response.text

print resp_xml
print "-----------------------------------------------\n"

xmls = ET.fromstring(resp_xml)

values = xmls.find('CallLineInfo/CallInfo/CallReference')			# loops over child elements of the values element
callRef = values.text
print values.text



# Answering call from phone_ip_2 (line 202)

api_url = 'https://{}/push' .format(phone_ip_2)
s_headers = {'Content-Type': 'application/x-com-polycom-spipx'}
s_data = ' <PolycomIPPhone><Data priority="Critical">CallAction:Answer;nCallReference={}</Data></PolycomIPPhone> ' .format(values.text)

response = requests.post(api_url, verify=False, auth=HTTPDigestAuth(user, pwd), headers=s_headers, data=s_data )

if (response.status_code == requests.codes.ok):
	print response.text
else:
	print 'Error! Status code: {}' .format(response.status_code)
	exit()







