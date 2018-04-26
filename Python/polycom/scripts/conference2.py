#!/usr/bin/env python
#
#	This script creates a conference - it works
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
phone_ip_3 = '10.1.0.11'		# vvx400

phone_no = '202'
phone_no_2 = '203'



# 1. Dial phone number from phone 1 (vvx 600)

api_url = 'https://{}/push' .format(phone_ip_1)
s_headers = {'Content-Type': 'application/x-com-polycom-spipx'}
s_data = ' <PolycomIPPhone><Data priority="Critical">tel:\\{}</Data></PolycomIPPhone> ' .format(phone_no)

response = requests.post(api_url, verify=False, auth=HTTPDigestAuth(user, pwd), headers=s_headers, data=s_data )


time.sleep(1)
# 2. Getting status from phone_ip_2

api_url = 'https://{}/polling/callstateHandler' .format(phone_ip_2)

response = requests.get(api_url, verify=False, auth=HTTPDigestAuth(user, pwd))
resp_xml = response.text

print resp_xml
print "-----------------------------------------------\n"

xmls = ET.fromstring(resp_xml)

values = xmls.find('CallLineInfo/CallInfo/CallReference')			# loops over child elements of the values element
callRef_p21 = values.text
print callRef_p21


time.sleep(1)
# 3. Answer call from phone 2

api_url = 'https://{}/push' .format(phone_ip_2)
s_headers = {'Content-Type': 'application/x-com-polycom-spipx'}
s_data = ' <PolycomIPPhone><Data priority="Critical">CallAction:Answer;nCallReference={}</Data></PolycomIPPhone> ' .format(callRef_p21)

response = requests.post(api_url, verify=False, auth=HTTPDigestAuth(user, pwd), headers=s_headers, data=s_data )

if (response.status_code == requests.codes.ok):
	print response.text
else:
	print 'Error! Status code: {}' .format(response.status_code)
	exit()


time.sleep(1)
# 4. Getting status from phone_ip_1

api_url = 'https://{}/polling/callstateHandler' .format(phone_ip_1)

response = requests.get(api_url, verify=False, auth=HTTPDigestAuth(user, pwd))
resp_xml = response.text

print resp_xml
print "-----------------------------------------------\n"

xmls = ET.fromstring(resp_xml)

values = xmls.find('CallLineInfo/CallInfo/CallReference')			# loops over child elements of the values element
callRef_p11 = values.text
print callRef_p11


time.sleep(1)
# 5. push conference button

api_url = 'https://{}/push' .format(phone_ip_1)
s_headers = {'Content-Type': 'application/x-com-polycom-spipx'}
s_data = ' <PolycomIPPhone><Data priority="Critical">CallAction:Conference;nCallReference={}</Data></PolycomIPPhone> ' .format(callRef_p11)

response = requests.post(api_url, verify=False, auth=HTTPDigestAuth(user, pwd), headers=s_headers, data=s_data )

if (response.status_code == requests.codes.ok):
	print response.text
else:
	print 'Error! Status code: {}' .format(response.status_code)
	exit()


time.sleep(1)
# 6. dial new number after sending conference message

s_data = ' <PolycomIPPhone><Data priority="Critical">tel:\\{}</Data></PolycomIPPhone> ' .format(phone_no_2)
response = requests.post(api_url, verify=False, auth=HTTPDigestAuth(user, pwd), headers=s_headers, data=s_data )

if (response.status_code == requests.codes.ok):
	print response.text
else:
	print 'Error! Status code: {}' .format(response.status_code)


time.sleep(1)
# 7. Getting status from phone_ip_3

api_url = 'https://{}/polling/callstateHandler' .format(phone_ip_3)

response = requests.get(api_url, verify=False, auth=HTTPDigestAuth(user, pwd))
resp_xml = response.text

print resp_xml
print "-----------------------------------------------\n"

xmls = ET.fromstring(resp_xml)

values = xmls.find('CallLineInfo/CallInfo/CallReference')			# loops over child elements of the values element
callRef_p31 = values.text
print callRef_p31


time.sleep(1)
# 8. answer from phone 3

api_url = 'https://{}/push' .format(phone_ip_3)
s_headers = {'Content-Type': 'application/x-com-polycom-spipx'}
s_data = ' <PolycomIPPhone><Data priority="Critical">CallAction:Answer;nCallReference={}</Data></PolycomIPPhone> ' .format(callRef_p31)

response = requests.post(api_url, verify=False, auth=HTTPDigestAuth(user, pwd), headers=s_headers, data=s_data )

if (response.status_code == requests.codes.ok):
	print response.text
else:
	print 'Error! Status code: {}' .format(response.status_code)
	exit()


time.sleep(1)
#9 Getting status from phone 1



time.sleep(1)
# 9. push conference button again, OR join calls

api_url = 'https://{}/push' .format(phone_ip_1)
s_headers = {'Content-Type': 'application/x-com-polycom-spipx'}
s_data = ' <PolycomIPPhone><Data priority="Critical">CallAction:Conference;nCallReference={}</Data></PolycomIPPhone> ' .format(callRef_p11)

response = requests.post(api_url, verify=False, auth=HTTPDigestAuth(user, pwd), headers=s_headers, data=s_data )

if (response.status_code == requests.codes.ok):
	print response.text
else:
	print 'Error! Status code: {}' .format(response.status_code)
	exit()







