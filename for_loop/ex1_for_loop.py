#  Write the program to print even number

print("code for even number: ")
N=int(input("N: "))
for i in range(1,N+1):
    if i%2==0:
        print(i)

print()          #use to give empty line
print()

#  Write program to print odd number
print("code for odd number: ")
N=int(input("N: "))
for i in range(1,N+1):
    if i%2!=0:
        print(i)


print()
print()

# Wrie the program to add n number of input by user
print("For adding n number of inputs ")
N=int(input("N: "))
sum=0
for i in range(N):
    user_input= int(input("Enter Your Value: "))
    sum=sum + user_input
print(sum)

