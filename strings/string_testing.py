print("Type '0' to end the loop\n")

while True:
    user_input = input("Type your string: ")

    if user_input == "0":
        break
    elif user_input.isalpha():
        print("Result: Yes, this is an alphabet")
    elif user_input.isdigit():
        print("Result: This is a digit")
    elif user_input.isalnum():
        print("Result: This is alpha-numeric")
    
    # Check if the input is a palindrome
    if user_input.lower() == user_input.lower()[::-1]:
        print("Result: This is a palindrome")
    else:
        print("Result: This is not a palindrome")
