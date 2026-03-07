'''
6-6. Polling: Use the code in favorite_languages.py (page 104) .
• Make a list of people who should take the favorite languages poll . Include
some names that are already in the dictionary and some that are not .
• Loop through the list of people who should take the poll . If they have already taken the poll, print a message thanking them for responding . If they have not yet taken the poll, print a message inviting them to take the poll .
'''

persons = ['sarah', 'jhon', 'kenny', 'phil']

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("\n")
for name in favorite_languages.keys():
    if name in persons:
        print(f"{name.title()},thank you for responding.You are already in the poll.")
    else:
        print(f"{name.title()}, I invite you to take the poll.")
        
print("\n")