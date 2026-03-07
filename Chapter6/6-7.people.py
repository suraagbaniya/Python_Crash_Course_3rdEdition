'''
6-7. People: Start with the program you wrote for Exercise 6-1 (page 102) . Make two new dictionaries representing different people, and store all three dictionaries in a list called people . Loop through your list of people . As you loop through the list, print everything you know about each person .
'''


people = {
    'jhon':{
        'first_name':'jhon',
        'last_name':'doe',
        'age':23,
        'city':'houston',
    },
    'jamie':{
        'first_name':'jamie',
        'last_name':'potter',
        'age':34,
        'city':'birmingham', 
    },
    'dave':{
        'first_name':'dave',
        'last_name':'water',
        'age':20,
        'city':'manchester', 
    }
}

for name, name_info in people.items():
    print(f"\n{name_info['first_name'].title()} {name_info['last_name'].title()} is {name_info['age']} and lives in {name_info['city'].title()}")