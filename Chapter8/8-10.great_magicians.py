'''
8-10. Great Magicians: Start with a copy of your program from Exercise 8-9 . Write a function called make_great() that modifies the list of magicians by add- ing the phrase the Great to each magician’s name . Call show_magicians() to see that the list has actually been modified .
'''

def make_great(magicianNames, newNames=[]):
    for eachName in magicianNames:
        temp = f"the Great {eachName}"
        newNames.append(temp)
    return newNames
        
def show_magicians(magicians):
    print("\n")
    for eachMagician in magicians:
        print(f"{eachMagician.title()}")

names = ["david blaine", "jeffrey", "liam"]

names = make_great(names)
show_magicians(names)
