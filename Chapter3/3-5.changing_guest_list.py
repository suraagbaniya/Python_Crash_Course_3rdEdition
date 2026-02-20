'''
3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations . You’ll have to think of someone else to invite .
• Start with your program from Exercise 3-4 . Add a print statement at the end of your program stating the name of the guest who can’t make it .
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting .
• Print a second set of invitation messages, one for each person who is still in your list .

'''

guests = ["buddha", "einstein", "newton"]
print(f"Hi {guests[0].title()}, you have been invited to my dinner party.")
print(f"Hi {guests[1].title()}, you have been invited to my dinner party.")
print(f"Hi {guests[2].title()}, you have been invited to my dinner party.")
print(f"\nNewton cannot make it to the dinner party.")

guests[2] = "tata"
print(f"\nHi {guests[0].title()}, you have been invited to my dinner party.")
print(f"Hi {guests[1].title()}, you have been invited to my dinner party.")
print(f"Hi {guests[2].title()}, you have been invited to my dinner party.")