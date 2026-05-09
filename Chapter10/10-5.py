"""
10-5. Programming Poll: Write a while loop that asks people why they like programming . Each time someone enters a reason, add their reason to a file that stores all the responses .
"""

filename = "Chapter10/programming_poll.txt"
flag = True

while flag:
    name = input("\nEnter your name: ")
    reason = input("Why do you like programming: ")
    with open(filename,'a') as file_object:
        file_object.write(f"{name.title()}\nReason: {reason}\n")
    
    print("\nEnter 'quit' if you want to quit.")
    print("Enter anything else if you want to continue.")
    flag = input("")
    
    if flag == 'quit':
        flag = False
    else:
        flag = True