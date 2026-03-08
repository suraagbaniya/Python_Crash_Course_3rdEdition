'''
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times . Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders . Make sure no pastrami sandwiches end up in finished_sandwiches .
'''

sandwich_orders = ["chicken sandwich","pastrami" ,"cheese sandwich", "veg sandwich", 'pastrami','pastrami']
finished_sandwich= []

print("Deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I have taken order for {current_sandwich}")
    
    finished_sandwich.append(current_sandwich) 
    
for eachSandwich in finished_sandwich:
    print(f"{eachSandwich} was made.")