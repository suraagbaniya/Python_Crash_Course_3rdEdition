'''
3-6. More Guests: You just found a bigger dinner table, so now more space is available . Think of three more guests to invite to dinner .
• Start with your program from Exercise 3-4 or Exercise 3-5 . Add a print statement to the end of your program informing people that you found a bigger dinner table .
• Use insert() to add one new guest to the beginning of your list .
• Use insert() to add one new guest to the middle of your list .
• Use append() to add one new guest to the end of your list .
• Print a new set of invitation messages, one for each person in your list .
'''

guests = ["buddha", "einstein", "newton"]
print(f"Hi {guests[0].title()}, you have been invited to my dinner party.")
print(f"Hi {guests[1].title()}, you have been invited to my dinner party.")
print(f"Hi {guests[2].title()}, you have been invited to my dinner party.")

print(f"\nThere is some good news. I have just found a bigger dinner table, so i will be inviting more guests.")

guests.insert(0, "messi")
guests.insert(2, "dalai")
guests.append("jordan")

print(f"Hi {guests[0].title()}, you have been invited to my dinner party.")
print(f"Hi {guests[1].title()}, you have been invited to my dinner party.")
print(f"Hi {guests[2].title()}, you have been invited to my dinner party.")
print(f"Hi {guests[3].title()}, you have been invited to my dinner party.")
print(f"Hi {guests[4].title()}, you have been invited to my dinner party.")
print(f"Hi {guests[5].title()}, you have been invited to my dinner party.")