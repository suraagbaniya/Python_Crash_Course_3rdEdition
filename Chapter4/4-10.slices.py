'''
4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
• Print the message, The first three items in the list are: . Then use a slice to print the first three items from that program’s list .
• Print the message, Three items from the middle of the list are: . Use a slice to print three items from the middle of the list .
• Print the message, The last three items in the list are: . Use a slice to print the last three items in the list .
'''

#created another separate list instead of working with the one i already made in this chapter

numbers = list(range(1,10))

print(f"The first three elements of list 'numbers' are {numbers[0:3]}")
print(f"The middle three elements of list 'numbers' are {numbers[3:6]}")
print(f"The last three elements of list 'numbers' are {numbers[6:9]}")