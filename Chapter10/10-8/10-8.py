"""
10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt . Store at least three names of cats in the first file and three names of dogs in the second file . Write a program that tries to read these files and print the contents of the file to the screen . Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing . Move one of the files to a dif- ferent location on your system, and make sure the code in the except block executes properly .
"""

filename = ["Chapter10/10-8/cats.txt", "Chapter10/10-8/dogs.txt"]

for eachfile in filename:
    try:
        with open (eachfile, 'r') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("Sorry. The file could not be found")