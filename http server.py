# Create a basic HTTP server that can handle GET and POST requests.
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

# Represents the creation of a new class named MyRequestHandler that inherits from the existing class SimpleHTTPRequestHandler.
# This task is done so that one can override (customize) specific methods in MyRequestHandler. Methods include do_GET and do_POST.
class MyRequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        # Handle GET requests the server receives
        if self.path == '/':
            # Sends an HTTP response header with a status code of 200, indicating a successful request.
            self.send_response(200)
            # Specifies the content type of the response as HTML (you can modify this header based on the type of content you are serving)
            # The HyperText Markup Language or HTML is the standard markup language for documents designed to be displayed in a web browser
            self.send_header('Content-type', 'text/html')
            # Marks the end of the response headers.
            self.end_headers()
            # Writes a response
            self.wfile.write(b'Hello, this is your HTTP server!')
        # Added new "route" '/about'. When a GET request is made to /about, the server responds with a message indicating that it's the About page.
        elif self.path == '/about':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'This is the About page.')
        else:
            # super() is a built-in function that returns a temporary object of the superclass, allowing you to call its methods.
            # In this example, if the requested path (self.path) is not '/', it falls back to the default behavior defined in the superclass (SimpleHTTPRequestHandler).
            super().do_GET()

    def do_POST(self):
        # Handle POST requests here
        # Added a new route '/submit' for handling POST requests
        if self.path == '/submit':
            # The 'Content-Length' header indicates the size (in bytes) of the message body in the HTTP request. self.headers['Content-Length'] retrieves the value of the 'Content-Length' header as a string and int convers it to an integer
            content_length = int(self.headers['Content-Length'])
            # self.rfile allows reading data from the request body. The received data is in bytes, so this method is used to decode the byte data into a UTF-8 encoded string. This is important when dealing with text-based data.
            post_data = self.rfile.read(content_length).decode('utf-8')

            # Parse the POST data (assuming it's in the form of key-value pairs)
            # parse_qs stands for "parse query string," and it is commonly used to parse data in the form of a URL-encoded query string.
            data_dict = parse_qs(post_data)

            # Process the received data (for demonstration purposes, just print it)
            print(f'Received POST data: {data_dict}')

            # Send a response to the client
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Thank you for submitting the data!')
        else:
            # Fallback to default behavior for other POST requests
            super().do_POST()


# Set up the server
port = 8000
server_address = ('', port)

# HTTPServer: This is a class provided by the http.server module in Python. It is used to create an HTTP server.
httpd = HTTPServer(server_address, MyRequestHandler)

print(f'Starting server on port {port}...')

# This method is called to start the server and make it listen for incoming requests indefinitely. 
httpd.serve_forever()