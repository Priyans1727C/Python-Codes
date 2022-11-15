a=int(input("rows: "))

#for lower pyramid 
print()
print()

for i in range(a):
    for j in range(i):
        print(" ",end="")
    for k in range(a-i):
        print("*",end=" ")
    print()

    print()
print()

# for upper pyramid

for i in range(a):
    for k in range(a-i-2,-1,-1):
        print(" ",end="")
    for l in range(i+1):
        print("*",end=" ")
    print()
