'''
7-10. Dream Vacation: Write a program that polls users about their dream vacation . Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll .
'''

vacation = input("\nIf you could visit any place, where would you go. Enter 'quit' to exit when you have listed all your places: ")

vacation_list=[]

while True:
    if vacation == 'quit': break
    vacation_list.append(vacation)
    
    vacation = input("\nIf you could visit any place, where would you go. Enter 'quit' to exit when you have listed all your places: ")
    
    
for eachVacationPlace in vacation_list:
    print(eachVacationPlace)