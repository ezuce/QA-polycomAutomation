#!/usr/bin/env python
#
#	This script creates a conference - it works
#



import polyOps			# module with defined functions

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



# 1. ---- Dial phone number from phone 1 (vvx 600)

response = polyOps.callNumber( phone_ip_1, phone_no )

if (response.status_code != requests.codes.ok):
	print 'Error! Status code: {}' .format(response.status_code)
	exit()
else:
	print '{}: dialing {}' .format(phone_ip_1, phone_no)


time.sleep(1)
# 2. ---- Getting status from phone_ip_2

callRef_p21 = polyOps.getCallId( phone_ip_2 )
print "Call ID for {} on {}: {}" .format(phone_no, phone_ip_2, callRef_p21)


time.sleep(1)
# 3. ---- Answer call from phone 2

response = polyOps.answerCall( phone_ip_2, callRef_p21 )

if (response.status_code != requests.codes.ok):
	print 'Error! Status code: {}' .format(response.status_code)
	exit()
else:
	print '{}: call answered' .format(phone_ip_2)


time.sleep(1)
# 4. ---- Getting status from phone_ip_1

callRef_p11 = polyOps.getCallId( phone_ip_1 )
print "Call ID for {} on {}: {}" .format(phone_no, phone_ip_1, callRef_p11)


time.sleep(1)
# 5. ---- Push conference button

response = polyOps.callConf( phone_ip_1, callRef_p11 )

if (response.status_code != requests.codes.ok):
	print 'Error! Status code: {}' .format(response.status_code)
	exit()
else:
	print 'Creating Conference...'


time.sleep(1)
# 6. ---- Dial new number after sending conference message

response = polyOps.callNumber( phone_ip_1, phone_no_2 )

if (response.status_code != requests.codes.ok):
	print 'Error! Status code: {}' .format(response.status_code)
else:
	print '{}: dialing {}' .format(phone_ip_1, phone_no_2)


time.sleep(1)
# 7. ---- Getting status from phone_ip_3

callRef_p31 = polyOps.getCallId( phone_ip_3 )
print "Call ID for {} on {}: {}" .format(phone_no_2, phone_ip_3, callRef_p31)


time.sleep(1)
# 8. ---- Answer from phone 3

response = polyOps.answerCall( phone_ip_3, callRef_p31 )

if (response.status_code != requests.codes.ok):
	print 'Error! Status code: {}' .format(response.status_code)
	exit()
else:
	print '{}: call answered' .format(phone_ip_3)


# time.sleep(1)
#9 Getting status from phone 1



time.sleep(1)
# 9. ---- Push conference button again, OR join calls

response = polyOps.callConf( phone_ip_1, callRef_p11 )

if (response.status_code != requests.codes.ok):
	print 'Error! Status code: {}' .format(response.status_code)
	exit()
else:
	print "Conference created."



# alternativa conferinta - stocheaza ambele call references si da-le






