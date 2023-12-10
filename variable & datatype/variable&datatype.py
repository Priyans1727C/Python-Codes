import sys

a = 30
b = "hello"
c = "30"
d = 71.2
e = True

# Printing data type of values assigned to variables a, b, c, d
# Using type() function:
print(type(a))  # integer
print(type(b))  # string
print(type(c))  # string -- anything inside double quotes is a string
print(type(d))  # float -- any decimal number is counted as a float
print(type(e))  # boolean -- this contains only True and False

# Print the size of each variable in terms of memory consumption
print(f"Size of variable 'a': {sys.getsizeof(a)} bytes")
print(f"Size of variable 'b': {sys.getsizeof(b)} bytes")
print(f"Size of variable 'c': {sys.getsizeof(c)} bytes")
print(f"Size of variable 'd': {sys.getsizeof(d)} bytes")
print(f"Size of variable 'e': {sys.getsizeof(e)} bytes")
