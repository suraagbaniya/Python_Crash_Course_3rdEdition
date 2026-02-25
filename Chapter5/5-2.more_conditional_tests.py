'''
5-2. More Conditional Tests: You don’t have to limit the number of tests you create to 10 . If you want to try more comparisons, write more tests and add them to conditional_tests.py . Have at least one True and one False result for each of the following:
• Tests for equality and inequality with strings
• Tests using the lower() function
• Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
'''

fruit = "banana"
print(fruit == "banana")
print(fruit != "banana")

print("\n")

animal = "Cat"
print(animal.lower() == "cat")
print(animal.lower() == animal)

print("\n")

number = 10

print(number == 10)
print(number != 10)

print(number > 1)
print(number < 1)

print(number >= 10)
print(number <=1 )


print("\n")
a = 1
b =2

print(a == 1 and b == 2)

print(a == 1 or b == 4)

clothes = ["jacket", "hoodie", "pant"]
print("jacket" in clothes)
print("shoes" in clothes)

print("\n")

print("tie" not in clothes)