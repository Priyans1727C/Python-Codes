import json

#Python Dict
pydict={'id':'1','name':'priyanshu','class':'09'}

print(f"pydict data type: {type(pydict)}\npydict dsta: {pydict}")


# Convert Python dict to JSON
json_data=json.dumps(pydict,indent=7)   #here indent is use for whitespace and data represention in batter way;
print(f"json_data data type: {type(json_data)}\njson_data data: {json_data}")