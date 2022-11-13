#  Write code to print sum of even number

print("code to calculate sum of even number  ")
N=int(input("N: "))
sum=0
for i in range(N+1):
    if i%2==0:
        sum=sum+i
print('sum:',sum)

print()
print()
print()


#  Write code to calculate sum of even number

print("code to calculate sum of even number")
N=int(input("N:"))
sum=0
for i in range(N+1):
    if i%2!=0:
        sum=sum+i
print("sum:", sum)