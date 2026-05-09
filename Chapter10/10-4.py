"""
10-4. Guest Book: Write a while loop that prompts users for their name . When they enter their name, print a greeting to the screen and add a line recording their visit in a file called guest_book.txt . Make sure each entry appears on a new line in the file .
"""

filename = "Chapter10/guest_book.txt"

print("\nEnter your name as many times as you like.")
print("Enter 'quit' when you are done.\n")
name = ""

while name != 'quit':
    name = input("Enter your name or 'quit' to exit: ")
    if name == 'quit':
        {
            print("EXITED")
        }
    else: 
        print(f"Hello {name}, welcome!!!")
        with open(filename, 'a') as file_object:
            file_object.write(f"{name.title()} was here.\n")
    