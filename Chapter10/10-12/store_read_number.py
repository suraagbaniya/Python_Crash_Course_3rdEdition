"""
10-12. Favorite Number Remembered: Combine the two programs from Exercise 10-11 into one file . If the number is already stored, report the favorite number to the user . If not, prompt for the user’s favorite number and store it in a file . Run the program twice to see that it works .
"""

import json

filename = "Chapter10/10-11/number.json"

def storeAndReadNumber(filename):
    try:
        with open(filename, 'r') as file_object:
            contents = json.load(file_object)
    except FileNotFoundError:
        favourite_number = input("\nWhat is your favorite number: ")
        with open(filename, 'w') as file_object:
            json.dump(favourite_number, file_object)
            print(f"We'll remember your favorite number {favourite_number} when you come back ")
    else:
        print(f"Your favourite number is {contents}")
        
storeAndReadNumber(filename)