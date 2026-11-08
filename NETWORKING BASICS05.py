#DAY - 34 - 35 
#HTTP/HTTPS Protocol - How web communicates
Hypertext Transfer Protocol is an application layer protocol that relies on a message-based, connectionless request-response model built on top of stateful TCP connections.
it siting on the 7th layer of OSI model, networking details are handled by lower layers, leaving HTTP traffic in readable plaintext. Everyline in an HTTP request or response is strictly termination by two ASCII Bytes Carriage Return.
HTTP Request consist of:
1. Request line - target path/resource, and http version
2. Headers - Key - value pairs providing metadata about the client and session
3. Mandatory blank line - Separates Headers from sqlite3 import _Parameters
from the body.
4. Optional body - contains submitted data(eg. post form parameters)

A STANDARD HTTP Response consists of:
1. The status line: Http version, a 3-digit status code and a text reason phrase
2.Headers: Metadata regarding server software cookies and content formatting 
3. Mandatory blank line followed by the Response body 

HTTP(PORT 80): Transmits messages over unencrypted TCP SOCKETS leaving requests and parameters visible to anyone packet snifffing the network path
HTTPS(PORT 443): Tunnels standard HTTP requests and responses through and encrypted ssl/tls transport layer the underlying http headers and payload logic remains identical but the transport pipelin is protected against non invasive interception


HTTP METHODS: Defining client Intent
http methods tell the web server what action to perform on a requested resources
GET (Retrieve Data):
 -Purpose - Fetches Resources from the web server without altering server state
 -Data Transmission - Appends parameters directly to the url string following a ?
 Security Concern - URLs containing GET query parameters are stored in browser history, written to server access logs, and transmitted to third-party sites via the Referer header. Sensitive data(such as passwords) should never be sent via GET

POST (send / submit data)
 -Purpose: Submits data to be processed by a specific server component(eg. authentification forms, file uploads, comment submissions)
  Data Transmission: Carries parameter payloads inside the http request body rather than in the URL query string.
  Security context - Browser do not automatically re-issue requests without warning the user because do so could duplicate actions.

POST (Replace / Upload Reseources)
 -Purpose: Uplaods or replaces a resource directly at the specified URL path using the request body payload.
 Security concern: Unrestricted or unauthenticated PUT permissions allow an auditor or attacker to upload arbitary executable scripts directly into the web root.

DELETE (Remove Resources)
 -Purpose: Requests that the server permanently remove the specified file or endpoint


HTTP Headers That Matter to Security Auditors
HTTP headers transmit metadata between client and server As noted in WAHH, developers sometimes mistakenly assume headers are tamper-proof making header manipulation a high-value auditing vector


HTTP Status Codes - Server Feedback
1xx(informational): Interim responses (eg. 100 Continue)
2xx(Success): Request was processed successfully 
3xx(Redirectional):(301 - Moved Permanently , 302 - Found)
4xx(Client Error): Request contains invalid syntax or unauthorized _Parameters
5xx(Server Error): An unhandled exception or backend error

Burp Suite Introduction & Interceptin Porxy Setup
intercepting Proxy - Intercepting proxy sits directly between your web browser and the target web application. Because all traffic passes through the proxy, it can stall every HTTP/HTTPS request and response in transit, allowing you to inspect, modify or drop packet parameters before they reach the network.
browser - burp proxy - Target web


1. Examine the raw request payload in Burp's Intercept window[32]:

```
POST /dvwa/login.php HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 ...
Content-Type: application/x-www-form-urlencoded
Content-Length: 47
Cookie: PHPSESSID=abc123xyz; security=low

username=admin&amp;password=wrongpassword&amp;Login=Login

