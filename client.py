import http.client

# Function to send a GET request
def send_get_request():
    conn_to_server = http.client.HTTPConnection("localhost", 8000)
    conn_to_server.request("GET", "/")
    response = conn_to_server.getresponse()
    print(f"GET Status: {response.status}")
    print(f"GET Reason: {response.reason}")
    data = response.read()
    print(f"GET Response: {data.decode()}")
    conn_to_server.close()

# Function to send a POST request
def send_post_request():
 
    conn_to_server = http.client.HTTPConnection("localhost", 8000)
    # Set the headers for the request
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    # Define the body of the request
    body = "name=John&age=30"
    conn_to_server.request("POST", "/", body, headers)
    response = conn_to_server.getresponse()
    print(f"POST Status: {response.status}")
    print(f"POST Reason: {response.reason}")
    data = response.read()
    print(f"POST Response: {data.decode()}")
    conn_to_server.close()

# Function to send a PUT request
def send_put_request():
   
    conn_to_server = http.client.HTTPConnection("localhost", 8000)
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    body ="name=alina&age=20"
    conn_to_server.request("PUT", "/", body, headers)
    response = conn_to_server.getresponse()
    print(f"PUT Status: {response.status}")
    print(f"PUT Reason: {response.reason}")
    data = response.read()
    print(f"PUT Response: {data.decode()}")
    conn_to_server.close()

# Function to send a HEAD request
def send_head_request():
    
    conn_to_server = http.client.HTTPConnection("localhost", 8000)
    conn_to_server.request("HEAD", "/")
    response = conn_to_server.getresponse()
    print(f"HEAD Status: {response.status}")
    print(f"HEAD Reason: {response.reason}")
    conn_to_server.close()

# Entry point of the script
if __name__ == "__main__":
    send_get_request()
    send_post_request()
    send_put_request()
    send_head_request()