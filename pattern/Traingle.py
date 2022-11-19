#Right angle traingle 

a=int(input("number of rows: "))
for i in range(a):
    for k in range(i+1):
        print("*",end=" ")
    print()

print()
print()


#lower traiangular

for i in range(a,0,-1):
    for k in range(i):
        print("*",end=" ")
    print()

print()
print()
