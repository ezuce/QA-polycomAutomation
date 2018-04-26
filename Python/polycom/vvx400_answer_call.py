# Answer incoming call from 10.1.0.11 with HTTPS curl
# curl --digest -u Push:Push -d  "<PolycomIPPhone><Data priority="Critical">Key:Softkey1</Data></PolycomIPPhone>" --header "Content-Type: application/x-com-polycom-spipx" https://10.1.0.14/push -k


import requests
import sys

from requests.auth import HTTPDigestAuth

user = "Push"
pwd = "Push"
phone_ip = '10.1.0.11'

api_url = 'https://{}/push' .format(phone_ip)
s_headers = {'Content-Type': 'application/x-com-polycom-spipx'}
s_data = ' <PolycomIPPhone><Data priority="Critical">Key:Softkey1</Data></PolycomIPPhone> '

response = requests.post(api_url, verify=False, auth=HTTPDigestAuth(user, pwd), headers=s_headers, data=s_data )

if (response.status_code == requests.codes.ok):
	print response.text
else:
	print 'Error! Status code: {}' .format(response.status_code)
