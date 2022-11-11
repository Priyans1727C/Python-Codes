# write a program to create list by user input (string only)

#solution =====

list=[]
print("")

print("0 to finish")
while True:
    a = input("Enter your elements: ")
    if a=="end":
        break
    list.append(a)


print("list =",list)