#!/usr/bin/env python
#
#	Get more details from status, also detect and print status changes
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


# Checking for status change from phone_ip_2

api_url='https://{}/polling/callstateHandler' .format(phone_ip_2)

linestate = "Inactive"

while 1:
	response = requests.get(api_url, verify=False, auth=HTTPDigestAuth(user, pwd))
	resp_xml = response.text

	xmls = ET.fromstring(resp_xml)
	ls = xmls.find('CallLineInfo/LineState')
	linestate = ls.text
	print linestate

	if (linestate == "Active"):
		calltype = xmls.find('CallLineInfo/CallInfo/CallType')
		callstate = xmls.find('CallLineInfo/CallInfo/CallState')
		callparty = xmls.find('CallLineInfo/CallInfo/CallingPartyDirNum')
		callref = xmls.find('CallLineInfo/CallInfo/CallReference')
		
		print "{} call: {} {} -> ref {}" .format(calltype.text, callstate.text, callparty.text, callref.text)
	time.sleep(1)


callref = xmls.find('CallLineInfo/CallInfo/CallReference')			# loops over child elements of the values element
																	# if status inactive it shows error < AttributeError: 'NoneType' object has no attribute 'text' >
print callref.text


