'''
6-3. Glossary: A Python dictionary can be used to model an actual dictionary . However, to avoid confusion, let’s call it a glossary .
• Think of five programming words you’ve learned about in the previous chapters . Use these words as the keys in your glossary, and store their meanings as values .
• Print each word and its meaning as neatly formatted output . You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line . Use the newline character (\n) to insert a blank line between each word-meaning pair in your output .
'''

glossary = {
    'list':'mutable ordered items',
    'tuple':'unmutable ordered items',
    'indentation':'4 spaces break',
    'if statement': 'statement to check whether a condition is true',
    'for loop': 'looping of certain tasks over a specified amount',
}

print(f"list : {glossary['list']}")
print(f"tuple : {glossary['tuple']}")
print(f"indentation : {glossary['indentation']}")
print(f"if statement : {glossary['if statement']}")
print(f"for loop : {glossary['for loop']}")