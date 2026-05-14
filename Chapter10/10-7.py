"""
10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop so the user can continue entering numbers even if they make a mistake and enter text instead of a number .
"""

flag = True
print("Enter 'q' to quit.")

while flag:
    number1 = input("\nEnter the first number: ")
    number2 = input("Enter the second number: ")
    
    if number1 == 'q' or number2 == 'q':
        flag = False
    
    else:   
        try:
            number1 = int(number1)
            number2 = int(number2)
        except ValueError:
            print("Sorry. Either one or both input is not a number.")
        else:
            print (number1+number2)