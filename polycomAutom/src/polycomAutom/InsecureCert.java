//
// This one works:
// http://www.nakov.com/blog/2009/07/16/disable-certificate-validation-in-java-ssl-connections/
//
// This class creates a trust manager that overrides certificate verification - allows "curl --insecure" 
//

package polycomAutom;

import java.security.cert.X509Certificate;

import javax.net.ssl.HostnameVerifier;
import javax.net.ssl.HttpsURLConnection;
import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLSession;
import javax.net.ssl.TrustManager;
import javax.net.ssl.X509TrustManager;

public class InsecureCert {
	
	// Constructorul creeaza un trust manager si permite rularea scriptului ca insecure	
	InsecureCert()
	{
		// Create a trust manager that does not validate certificate chains
		TrustManager[] trustAllCerts = new TrustManager[] {
			new X509TrustManager()
			{
				public java.security.cert.X509Certificate[] getAcceptedIssuers()
				{
					return null;
				}
				
				public void checkClientTrusted(X509Certificate[] certs, String authType) {
				}
							
				public void checkServerTrusted (X509Certificate[] certs, String authType) {
				}
			}								
		};
					
		// install the all-trusting trust manager
		try 
		{
			SSLContext sc = SSLContext.getInstance("SSL");
			sc.init(null, trustAllCerts, new java.security.SecureRandom() );
			HttpsURLConnection.setDefaultSSLSocketFactory( sc.getSocketFactory() );
		} catch (Exception e) {
		}
		
				
		// Create all-trusting host name verifier
		HostnameVerifier allHostsValid = new HostnameVerifier()
		{
			public boolean verify(String hostname, SSLSession session)
			{
				return true;
			}			
		};
		
		// Install the all-trusting host verifier
		HttpsURLConnection.setDefaultHostnameVerifier(allHostsValid);
		
		// Now you can access an https URL without having the certificate in the truststore		
	}
}

