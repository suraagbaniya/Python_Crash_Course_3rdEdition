'''
3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests .
• Start with your program from Exercise 3-6 . Add a new line that prints a message saying that you can invite only two people for dinner .
• Use pop() to remove guests from your list one at a time until only two names remain in your list . Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner .
• Print a message to each of the two people still on your list, letting them know they’re still invited .
• Use del to remove the last two names from your list, so you have an empty list . Print your list to make sure you actually have an empty list at the end of your program .
'''

guests = ["messi","buddha","dalai","einstein","newton","jordan"]

print("There has been some bad news.The dinner table which was said to arrive has now been cancelled.")


removedGuests = guests.pop()
print(f"\nWe are very sorry for the inconvinience {removedGuests.title()}")

removedGuests = guests.pop()
print(f"We are very sorry for the inconvinience {removedGuests.title()}")

removedGuests = guests.pop()
print(f"We are very sorry for the inconvinience {removedGuests.title()}")

removedGuests = guests.pop()
print(f"We are very sorry for the inconvinience {removedGuests.title()}")


print(f"\nHi {guests[0]}, you are still invited.")
print(f"Hi {guests[1]}, you are still invited.")

del(guests[0])
del(guests[0])

print("\n",guests)
