"""
9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you used a standard dictionary to represent a glossary . Rewrite the program using the OrderedDict class and make sure the order of the output matches the order in which key-value pairs were added to the dictionary .
"""

from collections import OrderedDict

glossary2 = OrderedDict()

glossary2['list'] = "mutable ordered items"
glossary2['tuple'] = "unmutable ordered items"
glossary2['indentation'] = "4 spaces break"
glossary2['if statement'] = "statement to check whether a condition is true"


for key,value in glossary2.items():
    print(f"{key.title()} : {value}")