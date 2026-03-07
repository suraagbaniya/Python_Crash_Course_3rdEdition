'''
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 102) by replacing your series of print statements with a loop that runs through the dictionary’s keys and values . When you’re sure that your loop works, add five more Python terms to your glossary . When you run your program again, these new words and meanings should automatically be included in the output .
'''

glossary2 = {
    'list':'mutable ordered items',
    'tuple':'unmutable ordered items',
    'indentation':'4 spaces break',
    'if statement': 'statement to check whether a condition is true',
    'for loop': 'looping of certain tasks over a specified amount',
    'zen of python': 'Conventions of python programming languages',
    'dataType': 'forms of data like integer, string etc',
}

for key,value in glossary2.items():
    print(f"{key.title()} : {value}")