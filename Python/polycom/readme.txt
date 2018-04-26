The following scripts have been written in python in order to automate calls on Polycom VVX400 phones.
For VVX500 and later phones (the ones with touchscreen), some functions could be a bit more difficult to implement due to limitations of touchscreen.

The following libraries have been used:
- Requests library was used to issue http commands to phones - run pip install requests
- Element Tree was used to parse the XML call state responses of the phones - default library

More information can be found on Polycom's support forum:
* https://community.polycom.com/t5/Polycom-End-Points-Forum/FAQ-Can-I-remotely-control-the-Phone-or-send-content-to-the/td-p/28596
* https://community.polycom.com/t5/Polycom-Endpoints-Forum/FAQ-Advanced-remote-control-possibilities-CTI/td-p/34836
* On the same forum: [FAQ] How can I check the status of a Polycom SoundPoint IP,
SoundStation IP or a VVX Phone?
* On the same forum: [FAQ] Can the Phone send Telephony Event Notifications?

