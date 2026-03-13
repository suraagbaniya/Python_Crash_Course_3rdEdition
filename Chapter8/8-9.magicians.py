'''
8-9. Magicians: Make a list of magician’s names . Pass the list to a function called show_magicians(), which prints the name of each magician in the list .
'''

def show_magicians(magicians):
    print("\n")
    for eachMagician in magicians:
        print(f"{eachMagician.title()}")

names = ["david blaine", "jeffrey", "liam"]
show_magicians(names)