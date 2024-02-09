# HTTP client that can make requests to your server and display the responses.

# install requests library
import requests

url = 'http://localhost:8000'  # Replace with your server's address

# Sending a GET request to the specified URL 
response_get = requests.get(url)
print(f'Status Code: {response_get.status_code}')
print(f'Headers: {response_get.headers}')
print(f'Response Body: {response_get.text}')

# Sending a POST request
# You can uncomment and modify this part if your server handles POST requests
# data = {'key': 'value'}
# response_post = requests.post(url, data=data)
# print(f'Response from server (POST): {response_post.text}')