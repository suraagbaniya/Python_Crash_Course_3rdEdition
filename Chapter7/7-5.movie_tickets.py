'''
7-5. Movie Tickets: A movie theater charges different ticket prices depending on a person’s age . If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15 . Write a loop in which you ask users their age, and then tell them the cost of their movie ticket .
'''

age = int(input('\nEnter your age: '))

while True:
    if age <3:
        print('You ticket price is FREE. you dont have to pay anything.')
    elif age<=12:
        print("Your ticket price is $10")
    else:
        print("Your ticket price is $15")
        
    age = int(input('\nEnter your age: '))