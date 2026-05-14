import json

filename = "Chapter10/10-11/number.json"

def read_number(filename):
    try:
        with open(filename, 'r') as file_object:
            contents = json.load(file_object)
    except FileNotFoundError:
        pass
    else:
        print(f"Your Favourite number is {contents}")

read_number(filename)