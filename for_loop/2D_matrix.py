rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(columns):
        element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
        row.append(element)
    matrix.append(row)

print("Entered Matrix:")
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
