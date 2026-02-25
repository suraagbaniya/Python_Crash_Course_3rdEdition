'''
5-13. Your Ideas: At this point, you’re a more capable programmer than you were when you started this book . Now that you have a better sense of how real-world situations are modeled in programs, you might be thinking of some problems you could solve with your own programs . Record any new ideas you have about problems you might want to solve as your programming skills con- tinue to improve . Consider games you might want to write, data sets you might want to explore, and web applications you’d like to create .
'''
score = 0
answers = []
# True or False Game

print("\n********** True Or False Game **********\n")
print("\n********** Enter T for True and F for False **********\n")

print("Q1. Is Pluto a part of Solar System")
answers.append (input("-> "))

print("\n")

print("Q2. Spiders have 8 legs")
answers.append (input("-> "))

print("\n")

print("Q3. Bee Hummingbird is the smallest bird in the world.")
answers.append (input("-> "))

print("\n")

print("Q4. Snails can sleep over 3 years")
answers.append (input("-> "))

print("\n")

print("Q5. Cheetah is the fastest land animal")
answers.append (input("-> "))

print("\n")


if answers:
    for answer in answers:
        if answer == "T" or "t":
            score = score+1


print(f"You scored {score} out of {len(answers)}")