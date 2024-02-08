import requests as req
import json

url= "https://httpbin.org/get"

payload={'key':'value','key2':'value2'}

r=req.get(url,params=payload)

print(r.url)

print(r.text)