# The program defines the basic functions used by polycom: call number, get status, answer call
# It reads the configuration from a config file.
#
#	TODO:	- add config file to read settings
#			- add function to return XML status


import requests
import sys
import time
import xml.etree.ElementTree as ET

from requests.auth import HTTPDigestAuth

from requests.packages.urllib3.exceptions import InsecureRequestWarning		#ignore warnings - not recommended
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

user = "Test"
pwd = "Test"
#phone_ip_1 = '10.1.0.14'
#phone_ip_2 = '10.1.0.12'		# vvx500




# ------ Call number function -----------
def callNumber( phone_ip, phone_no ):						# from which phone IP, to which number
	api_url = 'https://{}/push' .format(phone_ip)
	s_headers = {'Content-Type': 'application/x-com-polycom-spipx'}
	s_data = ' <PolycomIPPhone><Data priority="Critical">tel:\\{}</Data></PolycomIPPhone> ' .format(phone_no)
	return requests.post(api_url, verify=False, auth=HTTPDigestAuth(user, pwd), headers=s_headers, data=s_data )

# returns request response

#call_response = callNumber()
#if (call_response.status_code == requests.codes.ok):
#	print call_response.text
#else:
#	print 'Error! Status code: {}' .format(call_response.status_code)



# ------ Get status function -----------

def getCallId( phone_ip ):									# get status of which phone IP
	api_url='https://{}/polling/callstateHandler' .format( phone_ip )
	response = requests.get(api_url, verify=False, auth=HTTPDigestAuth(user, pwd))
	resp_xml = response.text

	return resp_xml

#xml_string = getCallId()
#print 'CallId: {}'	.format(resp_xml)


# ------ Get call ID function -----------

def getCallId( phone_ip ):									# get status of which phone IP
	api_url='https://{}/polling/callstateHandler' .format( phone_ip )
	response = requests.get(api_url, verify=False, auth=HTTPDigestAuth(user, pwd))
	resp_xml = response.text

	xmls = ET.fromstring(resp_xml)

	values = xmls.find('CallLineInfo/CallInfo/CallReference')			# loops over child elements of the values element
	#values = xmls.find('CallLineInfo/CallInfo/CallReference') # add vector and save other stuff
	callRef = values.text
	return values.text

#call_id_response = getCallId()
#print 'CallId: {}'	.format(call_id_response)



# ------ Answer call -----------

def answerCall( phone_ip, call_id ):						# from which phone IP, answer which call ID
	api_url = 'https://{}/push' .format( phone_ip )
	s_headers = {'Content-Type': 'application/x-com-polycom-spipx'}
	s_data = ' <PolycomIPPhone><Data priority="Critical">CallAction:Answer;nCallReference={}</Data></PolycomIPPhone> ' .format(call_id)
	return requests.post(api_url, verify=False, auth=HTTPDigestAuth(user, pwd), headers=s_headers, data=s_data )

# returns request response
#answer_response = answerCall()



# ------ Call on hold -----------

def callHold( phone_ip, call_id ):							# from which phone IP, put on hold call with which ID
	api_url = 'https://{}/push' .format( phone_ip )
	s_headers = {'Content-Type': 'application/x-com-polycom-spipx'}
	s_data = ' <PolycomIPPhone><Data priority="Critical">CallAction:Hold;nCallReference={}</Data></PolycomIPPhone> ' .format(call_id)
	return requests.post(api_url, verify=False, auth=HTTPDigestAuth(user, pwd), headers=s_headers, data=s_data )

# returns request response
#callHold_response = callHold()


# ------ Call resume -----------

def callResume( phone_ip, call_id ):						# from which phone IP, resume call with which ID
	api_url = 'https://{}/push' .format( phone_ip )
	s_headers = {'Content-Type': 'application/x-com-polycom-spipx'}
	s_data = ' <PolycomIPPhone><Data priority="Critical">CallAction:Resume;nCallReference={}</Data></PolycomIPPhone> ' .format(call_id)
	return requests.post(api_url, verify=False, auth=HTTPDigestAuth(user, pwd), headers=s_headers, data=s_data )

# returns request response
#callResume_response = callResume()



# ------ Set Conference -----------

def callConf( phone_ip, call_id ):							# from which phone IP, put on hold call with which ID
	api_url = 'https://{}/push' .format( phone_ip )
	s_headers = {'Content-Type': 'application/x-com-polycom-spipx'}
	s_data = ' <PolycomIPPhone><Data priority="Critical">CallAction:Conference;nCallReference={}</Data></PolycomIPPhone> ' .format(call_id)
	return requests.post(api_url, verify=False, auth=HTTPDigestAuth(user, pwd), headers=s_headers, data=s_data )




# ------ End Call -----------

def endCall( phone_ip, call_id ):							# from which phone IP, end call with which ID
	api_url = 'https://{}/push' .format( phone_ip )
	s_headers = {'Content-Type': 'application/x-com-polycom-spipx'}
	s_data = ' <PolycomIPPhone><Data priority="Critical">CallAction:EndCall;nCallReference={}</Data></PolycomIPPhone> ' .format(call_id)
	return requests.post(api_url, verify=False, auth=HTTPDigestAuth(user, pwd), headers=s_headers, data=s_data )


# returns request response
#endCall_response = endCall()









