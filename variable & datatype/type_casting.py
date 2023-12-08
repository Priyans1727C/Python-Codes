def add_feature(variable):
    # Check the current data type
    original_type = type(variable)

    # Perform the data type conversion
    if original_type == int:
        variable = str(variable)
    elif original_type == str:
        # Add the feature for strings (e.g., concatenate a string)
        variable += " NewFeature"

    # Print the new data type
    print(f"New data type of variable: {type(variable)}")

    # Print the variable with the added feature
    print(f"Variable with added feature: {variable}")

a = 30
b = "Harsh"
print(type(a))  


add_feature(a)
add_feature(b)
