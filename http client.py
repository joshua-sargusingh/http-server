# HTTP client that can make requests to your server and display the responses.

# install requests library
import requests

# Replace with your server's address
url = 'http://localhost:8000' 

# Sending a GET request to the specified URL 
response_get = requests.get(url)
print(f'Status Code: {response_get.status_code}')
print(f'Headers: {response_get.headers}')
print(f'Response Body: {response_get.text}')


# Replace with your server's address
url = 'http://localhost:8000/about' 

# Sending a GET request to the specified URL 
response_get = requests.get(url)
print(f'Status Code: {response_get.status_code}')
print(f'Headers: {response_get.headers}')
print(f'Response Body: {response_get.text}')


# Server URL and endpoint for handling POST requests
url = 'http://localhost:8000/submit'

# Data to be sent in the POST request. In this case, it's a dictionary with key-value pairs
data = {
    'name': 'Joshua Sargusingh',
    'age': 26,
    'city': 'Ottawa'
}

# Making the POST request
response_post = requests.post(url, data=data)

# Displaying the response from the server
print(f'Response Status Code: {response_post.status_code}')
print('Response Content:')
print(response_post.text)