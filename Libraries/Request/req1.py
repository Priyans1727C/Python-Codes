import requests as req
import json

post_req_url= "https://httpbin.org/anything"


r=req.get(post_req_url)

#by default it contain json file
print(r.text)

#printing in json format
# print(r.json())

#making post request here
post_req= req.put(post_req_url,data={'name':'thakur','name2':'ankur'})


print(post_req.text)
