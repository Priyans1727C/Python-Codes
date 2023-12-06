# Original lists
list = [1, 4, 5, 6, 7, 5]
list2 = ["ram", "harsh", "Subham"]
list3 = ["ram", 46, "yjugr", 2.00, "ehgrg"]

# Display original lists
print("Original list:", list)
print("Original list2:", list2)
print("Original list3:", list3)

# Function to calculate the sum of a list
def calculate_sum(input_list):
    if all(isinstance(x, (int, float)) for x in input_list):
        return sum(input_list)
    else:
        return "Cannot calculate sum for non-numeric elements."

# Calculate and print the sum of each list
print("Sum of list:", calculate_sum(list))
print("Sum of list2:", calculate_sum(list2))
print("Sum of list3:", calculate_sum(list3))
