'''
7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop .
• Use an active variable to control how long the loop runs .
• Use a break statement to exit the loop when the user enters a 'quit' value .
'''

age = int(input('\nEnter your age: '))

#Version1
a = 1
while a<=2:
    if age <3:
        print('You ticket price is FREE. you dont have to pay anything.')
    elif age<=12:
        print("Your ticket price is $10")
    else:
        print("Your ticket price is $15")
        
    age = int(input('\nEnter your age: '))
    
    a +=1
    
#Version2
age = int(input('\nEnter your age: '))
active = True

while active:
    if age <3:
        print('You ticket price is FREE. you dont have to pay anything.')
    elif age<=12:
        print("Your ticket price is $10")
    elif age<=100:
        print("Your ticket price is $15")
    else:
        active = False
        
    age = int(input('\nEnter your age: '))
    

#Version3
age = input('\nEnter "quit" to exit or Enter your age: ')

while True:
    
    if age == 'quit': 
        break
    else:
        age = int(age)
    
    if age <3:
                print('Your ticket price is FREE. you dont have to pay anything.')
    elif age<=12:
                print("Your ticket price is $10")
          
    else:   
               print("Your ticket price is $15") 
    
    
    
    age = input('\nEnter "quit" to exit or Enter your age: ')