import json

def read_and_print_json(file_path):
    with open(file_path, "r") as f:
        json_data = json.load(f)

    # Print the JSON data with an indentation of 7
    print(json.dumps(json_data, indent=7))

# Your existing code
table = {
    'data1': {
        'id': 1,
        'name': 'priyanshu',
        'class': 9
    },
    'data2': {
        'id': 2,
        'name': 'harsh',
        'class': 10
    }
}

data = json.dumps(table, indent=5)

with open("file.json", "w") as f:
    f.write(data)

# Call the new function to read and print the JSON data
read_and_print_json("file.json")
