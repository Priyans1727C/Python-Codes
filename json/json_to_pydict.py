import json

# JSON string
emp = '{"id":"1","name":"priyanshu","class":"09"}'
# print(emp)
print("emp: \n", emp, "\n", type(emp))

# Function to print specific information about the employee dictionary
def print_employee_info(employee_dict):
    print("Employee Information:")
    print("ID:", employee_dict.get("id"))
    print("Name:", employee_dict.get("name"))
    print("Class:", employee_dict.get("class"))

# print(help(json))

emp_dict = json.loads(emp)  # Convert string to Python dict

print(emp_dict)

# Call the new function to print specific information about the employee dictionary
print_employee_info(emp_dict)
