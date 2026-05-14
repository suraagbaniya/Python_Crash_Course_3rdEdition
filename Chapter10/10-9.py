"""
10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail silently if either file is missing .
"""

filename = ["Chapter10/10-8/cats.txt", "Chapter10/10-8/dogs.txt"]

for eachfile in filename:
    try:
        with open (eachfile, 'r') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass