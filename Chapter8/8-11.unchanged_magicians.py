'''
8-11. Unchanged Magicians: Start with your work from Exercise 8-10 . Call the function make_great() with a copy of the list of magicians’ names . Because the original list will be unchanged, return the new list and store it in a separate list . Call show_magicians() with each list to show that you have one list of the origi- nal names and one list with the Great added to each magician’s name .
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

show_magicians(make_great(names[:]))
show_magicians(names)
