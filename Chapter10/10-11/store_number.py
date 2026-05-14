"""
10-11. Favorite Number: Write a program that prompts for the user’s favorite number . Use json.dump() to store this number in a file . Write a separate pro- gram that reads in this value and prints the message, “I know your favorite number! It’s _____ .”
"""

import json

filename = "Chapter10/10-11/number.json"

favourite_number = input("\nWhat is your favorite number: ")
def storeNumber(filename):
    try:
        with open(filename, 'w') as file_object:
            json.dump(favourite_number, file_object)
    except FileNotFoundError:
        print("File not found.")
        
storeNumber(filename)