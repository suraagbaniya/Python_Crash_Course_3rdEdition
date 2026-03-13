'''
8-6. City Names: Write a function called city_country() that takes in the name of a city and its country . The function should return a string formatted like this:
     "Santiago, Chile"
Call your function with at least three city-country pairs, and print the value that’s returned .
'''


def city_country(city,country):
    full_name = (f"\n{city.title()}, {country.title()}")
    return full_name

print(city_country("kathmandu","nepal"))
print(city_country("new delhi","india"))
print(city_country("oslo","norway"))
