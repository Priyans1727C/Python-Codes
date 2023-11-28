import json

# JSON string
emp='{"id":"1","name":"priyanshu","class":"09"}'
# print(emp)
print("emp: \n",emp,"\n",type(emp))

# print(help(json))

emp_dict=json.loads(emp)   # Convert string to Python dict

print(emp_dict)
