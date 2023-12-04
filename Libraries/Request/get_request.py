import requests as req

# URL for basic authentication
url_auth = "https://httpbin.org/basic-auth/user/pass"

# URL for a GET request with parameters
url_get = "https://httpbin.org/get"

# Basic authentication
response_auth = req.get(url_auth, auth=('user', 'pass'))
print("Authentication Status Code:", response_auth.status_code)
print("Authentication Response:", response_auth.json())
print()

# GET request with parameters
payload = {'key': 'value', 'key2': 'value2'}
response_get = req.get(url_get, params=payload)
print("GET Request URL:", response_get.url)
print("GET Request Response:", response_get.text)
