# 0x10. Python - Network #0
## Hypertext Transfer Protocol (HTTP)

### What is HTTP?
- HTTP (Hypertext Transfer Protocol) is a protocol used for transmitting data over the internet. It is the foundation of data communication on the World Wide Web.

### HTTP Methods:
- HTTP defines several methods that indicate the desired action to be performed on a resource. Common methods include:
  - GET: Retrieves data from a specified resource.
  - POST: Submits data to be processed to a specified resource.
  - PUT: Updates a specified resource with new data.
  - DELETE: Deletes a specified resource.
  - And more: OPTIONS, HEAD, PATCH, etc.

### Features of HTTP:
- Stateless: HTTP is stateless, meaning each request from a client to a server is treated independently, without any memory of previous requests.
- Connectionless: Each request-response cycle in HTTP occurs independently of other cycles, and the connection is closed after each response.

### HTTP Header Fields:
- HTTP messages consist of header fields that provide additional information about the message. Header fields include:
  - Request headers: Sent by the client to the server.
  - Response headers: Sent by the server to the client.
  - Common headers: Content-Type, Content-Length, Cache-Control, User-Agent, etc.

### HTTP Status Codes:
- HTTP responses include status codes that indicate the result of the request. Common status codes include:
  - 200 OK: The request was successful.
  - 404 Not Found: The requested resource could not be found.
  - 500 Internal Server Error: The server encountered an unexpected condition.
  - And others: 301, 403, 502, etc.

### Uniform Resource Locator (URL):
- A URL is a reference to a web resource that specifies its location on the internet. It consists of several components, including the scheme, host, path, query parameters, and fragment.

### HTTP Basic Terms:
- URL (Uniform Resource Locator): A web address that specifies the location of a resource on the internet.
- Encryption: The process of encoding data to protect it from unauthorized access. HTTPS (HTTP Secure) is a secure version of HTTP that uses encryption.

### cURL (Command Line Tool):
- cURL is a command-line tool for transferring data with URLs. It supports various protocols, including HTTP, HTTPS, FTP, and more.
- With cURL, users can make HTTP requests, specify request methods, include headers, handle cookies, follow redirects, and more.

### Diagram of HTTP Protocol:
![HTTP Protocol Diagram](https://quickshare.samsungcloud.com/uo9nAAIyK3Bh)

