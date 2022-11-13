'''
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
'''

#Example: to print natural number 1-n

n=int(input("n: "))
for i in range(n+1):  #range does is one less then upper limits
    print(i)

#we can also use for loop in string and list as show below:

#for string

string=input("string: ")     #By deafult input type is string in python
for k in string:
    print(k)

print()
print()
print()         #used for creating empty

# for list:
 
my_list = ["harry","ram","sonu","raju","pawan"]
print("my_list",my_list) 

for j in my_list:
    print(j)