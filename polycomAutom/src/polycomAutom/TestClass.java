//
// WARNING: Phone state polling, PUSH and REST API need to be enabled and configured with a username/password on the polycom phones!
//

package polycomAutom;

import java.io.IOException;

public class TestClass {
	
	private static String PHONE_STATE_URL = "https://10.1.0.14/polling/callstateHandler";
	private static String PHONE_PUSH_URL = "https://10.1.0.14/push";
	private static String DELETE_URL = "https://10.1.0.14/push";
	private static String uname = "test";
	private static String passwd = "test";

	// phone call parameters
	private static String phone_no = "202";
	private static String header_call = "application/x-com-polycom-spipx";
	private static String payload_call = "<PolycomIPPhone><Data priority='\"Critical\"'>tel:\\" + phone_no + "</Data></PolycomIPPhone>";


	public static void main(String[] args) throws IOException
	{
		httpRequests req = new httpRequests();
		
		String statusGET = req.httpGET(PHONE_STATE_URL, uname, passwd);
		System.out.println(statusGET);
		System.out.println("\n GET done \n");
			
		// Format is: httpPOST(URL, username, password, header (content type), payload.
		// Can set "" instead of username, password, header and payload to not use the options
		String statusPOST = req.httpPOST(PHONE_PUSH_URL, uname, passwd, header_call, payload_call);
		System.out.println(statusPOST);
		System.out.println("\n POST done \n");			
	}

}
