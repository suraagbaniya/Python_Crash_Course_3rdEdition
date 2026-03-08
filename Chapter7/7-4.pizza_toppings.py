'''
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value . As they enter each topping, print a message saying you’ll add that topping to their pizza .
'''

topping = input('\nEnter a topping you want to add in your pizza.\nIf you are done adding type "quit": ')


while topping != 'quit':
    print(f"\nYou have added {topping} to your pizza.")
    
    topping = input('\nEnter a topping you want to add in your pizza.\nIf you are done adding type "quit": ')