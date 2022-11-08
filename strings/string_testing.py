print()
print("Type '0' to end the loop")
print("")
while True:
    a=input("Type your string: ")
    if a=="0":
        break
    elif a.isalpha()==True:
        print("Result: Yes this is alphabet")
    elif a.isdigit()==True:
        print("Result: This is Digit ")
    elif a.isalnum()==True:
        print("Result: This is Alpha-numeric")

