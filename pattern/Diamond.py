def print_diamond(rows):
    for i in range(1, rows + 1):
  
        for j in range(rows - i):
            print(" ", end="")
     
        for k in range(2 * i - 1):
            print("*", end="")
        print()

    for i in range(rows - 1, 0, -1):
        
        for j in range(rows - i):
            print(" ", end="")
        
        for k in range(2 * i - 1):
            print("*", end="")
        print()

n=int(input("a: "))
print_diamond(5)
