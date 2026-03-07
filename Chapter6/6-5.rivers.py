'''
6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through . One key-value pair might be 'nile': 'egypt' .
• Use a loop to print a sentence about each river, such as The Nile runs through Egypt .
• Use a loop to print the name of each river included in the dictionary .
• Use a loop to print the name of each country included in the dictionary .
'''

rivers_country = {
    'nile': 'egypt',
    'bagmati':'nepal',
    'gandaki':'nepal',
    }

for river,country in rivers_country.items():
    print(f"{river.title()} runs through {country.title()}")
    

for river in rivers_country.keys():
    print(river)
    
for country in rivers_country.values():
    print(country)