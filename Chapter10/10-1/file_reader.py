"""
10-1. Learning Python: Open a blank file in your text editor and write a few lines summarizing what you’ve learned about Python so far . Start each line with the phrase In Python you can... . Save the file as learning_python.txt in the same directory as your exercises from this chapter . Write a program that reads the file and prints what you wrote three times . Print the contents once by read- ing in the entire file, once by looping over the file object, and once by storing the lines in a list and then working with them outside the with block .
"""

with open('Chapter10/10-1/learning_python.txt') as text_object:
    contents = text_object.read().strip()
    print(contents)
    
print()

with open('Chapter10/10-1/learning_python.txt') as text_object:   
    for eachline in text_object:
        print(eachline.strip())
        
print()

with open('Chapter10/10-1/learning_python.txt') as text_object:   
    contents = text_object.readlines()
    text_list = contents
    
for eachitem in text_list:
    print(eachitem.strip())