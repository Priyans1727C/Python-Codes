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


# Calculate and display the sum of all elements in the matrix
matrix_sum = sum(sum(row) for row in matrix)
print(f"Sum of all elements in the matrix: {matrix_sum}")

# Calculate and display the transpose of the matrix
transpose_matrix = [[matrix[j][i] for j in range(rows)] for i in range(columns)]
print("Transpose of the matrix:")
for row in transpose_matrix:
    for element in row:
        print(element, end=' ')
    print()
