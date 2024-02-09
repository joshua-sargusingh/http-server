# Create a basic HTTP server that can handle GET requests. You can extend it to handle POST requests, serve static files, and implement basic routing.

from http.server import SimpleHTTPRequestHandler, HTTPServer

# Represents the creation of a new class named MyRequestHandler that inherits from the existing class SimpleHTTPRequestHandler.
# This taks is done so that one can override (customize) specific methods in MyRequestHandler. Methods include do_GET and do_POST.
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

            #Writes a response
            self.wfile.write(b'Hello, this is your HTTP server!')
        else:
            # super() is a built-in function that returns a temporary object of the superclass, allowing you to call its methods.
            # In this example, if the requested path (self.path) is not '/', it falls back to the default behavior defined in the superclass (SimpleHTTPRequestHandler).
            super().do_GET()

    def do_POST(self):
        # Handle POST requests here if needed
        pass

# Set up the server
port = 8000
server_address = ('', port)

# HTTPServer: This is a class provided by the http.server module in Python. It is used to create an HTTP server.
httpd = HTTPServer(server_address, MyRequestHandler)

print(f'Starting server on port {port}...')

# This method is called to start the server and make it listen for incoming requests indefinitely. 
httpd.serve_forever()