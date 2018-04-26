//
//	Equivalent of GET, POST and DELETE methods from CURL, using insecure and digest authentication 
//

package polycomAutom;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;

import javax.net.ssl.HttpsURLConnection;

import java.net.Authenticator;
import java.net.PasswordAuthentication;
import java.net.URL;


public class httpRequests {
	
	public String httpGET(String url, String username, String password) throws IOException
	{
		InsecureCert insc = new InsecureCert();

		// Declare a new object with GET parameter
		URL obj = new URL(url);
		HttpsURLConnection con = (HttpsURLConnection) obj.openConnection();
		con.setRequestMethod("GET");
		
		// standard authentication
		//String basicAuth = "Basic " + javax.xml.bind.DatatypeConverter.printBase64Binary(userpass.getBytes());
		//con.setRequestProperty("Authorization", basicAuth);
		
		// authentication with Authenticator - HttpsURLConnection cannot use digest by default!
		if( (username == "" && password == "") )
		{
			System.out.println("No username / password provided");
		}
				
		else
		{
			Authenticator.setDefault(new Authenticator() { 
			    protected PasswordAuthentication getPasswordAuthentication() { 
		    	return new PasswordAuthentication(username, password.toCharArray()); 
			    } 
			}); 
		}	
		
		int responseCode = con.getResponseCode();
		System.out.println("GET Response Code :: " + responseCode);
		
		
		if(responseCode == HttpsURLConnection.HTTP_OK)
		{	// success
			BufferedReader in = new BufferedReader ( new InputStreamReader (con.getInputStream()) );
			String inputLine;
			
			StringBuffer response = new StringBuffer();
			
			while ( (inputLine = in.readLine()) != null )
			{
				response.append(inputLine);
			}
			
			// print result
			return (response.toString());
		}
		
		else
		{	// Returns a certain error
			return "GET request not worked";
		}
	}
	
	
	public String httpPOST(String url, String username, String password, String header, String payload) throws IOException
	{
		InsecureCert insc = new InsecureCert();

		// Declare a new object with POST parameter
		URL obj = new URL(url);
		HttpsURLConnection con = (HttpsURLConnection) obj.openConnection();
		con.setRequestMethod("POST");
		
		// standard authentication
		//String basicAuth = "Basic " + javax.xml.bind.DatatypeConverter.printBase64Binary(userpass.getBytes());
		//con.setRequestProperty("Authorization", basicAuth);
		
		
		// authentication with Authenticator - HttpsURLConnection cannot use digest by default!
		if( (username == "" && password == "") )
		{
			System.out.println("No username / password provided");
		}
		
		else
		{
			Authenticator.setDefault(new Authenticator() { 
			    protected PasswordAuthentication getPasswordAuthentication() { 
			    	return new PasswordAuthentication(username, password.toCharArray()); 
			    } 
			}); 
		}		
		
		// Add content type header
		if(header == "")
		{
			System.out.println("Content type header null");
		}
		
		else
		{
			con.setRequestProperty("Content-Type", header);		
		}
		
		// Add payload if not null
		if(payload == "")
		{
			System.out.println("Payload null");			
		}
		
		else
		{
			con.setDoOutput(true);
			OutputStream outputStream = con.getOutputStream();
            outputStream.write(payload.getBytes("UTF-8"));
            outputStream.close();
		}
		
		int responseCode = con.getResponseCode();
		System.out.println("POST Response Code :: " + responseCode);
		
		
		if(responseCode == HttpsURLConnection.HTTP_OK)
		{	// success
			BufferedReader in = new BufferedReader ( new InputStreamReader (con.getInputStream()) );
			String inputLine;
			
			StringBuffer response = new StringBuffer();
			
			while ( (inputLine = in.readLine()) != null )
			{
				response.append(inputLine);
			}
			
			// print result
			return (response.toString());
		}
		
		else
		{	// Returns a certain error
			return "POST request not worked";
		}
		
	}
	
	// untested
	public String httpDELETE(String url, String username, String password) throws IOException
	{
		InsecureCert insc = new InsecureCert();

		// Declare a new object with DELETE parameter
		URL obj = new URL(url);
		HttpsURLConnection con = (HttpsURLConnection) obj.openConnection();
		con.setRequestMethod("DELETE");
		
		// standard authentication
		//String basicAuth = "Basic " + javax.xml.bind.DatatypeConverter.printBase64Binary(userpass.getBytes());
		//con.setRequestProperty("Authorization", basicAuth);
		
		// authentication with Authenticator - HttpsURLConnection cannot use digest by default!
		if( (username == "" && password == "") )
		{
			System.out.println("No username / password provided");
		}
		
		else
		{
			Authenticator.setDefault(new Authenticator() { 
			    protected PasswordAuthentication getPasswordAuthentication() { 
			    	return new PasswordAuthentication(username, password.toCharArray()); 
			    } 
			}); 
		}	
		
		int responseCode = con.getResponseCode();
		System.out.println("DELETE Response Code :: " + responseCode);
		
		
		if(responseCode == HttpsURLConnection.HTTP_OK)
		{	// success
			BufferedReader in = new BufferedReader ( new InputStreamReader (con.getInputStream()) );
			String inputLine;
			
			StringBuffer response = new StringBuffer();
			
			while ( (inputLine = in.readLine()) != null )
			{
				response.append(inputLine);
			}
			
			// print result
			return (response.toString());
		}
		
		else
		{	// Returns a certain error
			return "DELETE request not worked";
		}
	}
	
}
