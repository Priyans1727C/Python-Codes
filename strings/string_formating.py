a = input("Type your string: ")
b = int(input("Width value: "))
fill_char = input("Fill character: ")

print("Centered:".ljust(10), a.center(b, fill_char))
print("Left-justified:".ljust(10), a.ljust(b, fill_char))
print("Right-justified:".ljust(10), a.rjust(b, fill_char))
