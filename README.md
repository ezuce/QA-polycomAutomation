# QA-polycomAutomation

* Python/polycom - contains Python scripts for some functions of Polycom phones
* polycomAutom - contains a Java implementation of HTTP Get, Post and Delete, usable to write scripts for polycom phones

The phones need to be configured as following for the scripts to work:
* Open up the phone configuration page in a browser (https://phone_IP, default password 456)
* In Settings - Applications configure the phone, as following:
  -  Phone State Polling - Response Mode - Requester, pick a username and password to use
  -  Push - Allow push messages, pick a username and password to use
  -  Rest API - enabled
