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

#up right triangle

for i in range(a):
    for k in range(a-i-2,-1,-1):
        print(" ",end=" ")
    for s in range(i):
        print("*",end=" ")
    print()

print()
print()

#down right triangle

for i in range(a):
    for k in range(i):
        print(" ",end=" ")
    for s in range(a-i):
        print("*",end=" ")
    print()

print()
print()
