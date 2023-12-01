import requests as req

url="https://httpbin.org/basic-auth/user/pass"


#normal get request
# response=req.get(url)

#Get request with authentication
response=req.get(url,auth=('user','pass'))

print(response.status_code)

print(response.json())


url2= "https://httpbin.org/get"
payload={'key':'value','key2':'value2'}

#get request with paramaters
r=req.get(url2,params=payload)

print(r.url)

print(r.text)
