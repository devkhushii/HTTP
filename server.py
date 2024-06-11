from http.server import BaseHTTPRequestHandler, HTTPServer

# Define a custom HTTP request handler class
class HTTPREQUEST(BaseHTTPRequestHandler):

    # Handle GET requests
    def do_GET(self):
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        fin = open('index.html')
        response = fin.read()
        fin.close()
        self.wfile.write(response.encode())
        print("GET request resolved")

    # Handle POST requests
    def do_POST(self):
        
        # Get the length of the data sent in the request
        content_length = int(self.headers['Content-Length'])
        # Read the data sent in the request body
        data = self.rfile.read(content_length)
        print(f"Received POST: {data.decode()}")
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        response = "Data received"
        self.wfile.write(response.encode())
        self.wfile.write(b"POST request received!")
        print("POST request resolved")

    # Handle PUT requests
    def do_PUT(self):
       
        # Get the length of the data sent in the request
        content_length = int(self.headers['Content-Length'])
        # Read the data sent in the request body
        put_data = self.rfile.read(content_length)
        print(f"Received PUT: {put_data.decode()}")
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        response = "Data received and updated"
        self.wfile.write(response.encode())
        print("PUT request resolved")

    # Handle HEAD requests
    def do_HEAD(self):
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        print("HEAD request resolved")

# Function to run the HTTP server
def run(server_class=HTTPServer, handler_class=HTTPREQUEST, port=8000):
    # Define the server address and port
    server_address = ('', port)
    
    # Create an instance of the server
    http_instance = server_class(server_address, handler_class)
    print(f"Starting http server on port {port}")
    # Start the server to handle requests indefinitely
    http_instance.serve_forever()

# Entry point of the script
if __name__ == "__main__":
    # Run the server
    run()
