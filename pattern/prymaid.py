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
