'''
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so each person can have more than one favorite number . Then print each person’s name along with their favorite numbers .
'''

favorite_numbers = {
    'jhon':[10,3,7],
    'sarah':[0,8,1],
    'huber':[39,5]
}

for person,numbers in favorite_numbers.items():
    print(f"\n{person.title()}'s favorite numbers are: ")
    for number in numbers:
        print(number)