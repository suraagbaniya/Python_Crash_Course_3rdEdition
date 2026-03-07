'''
6-11. Cities: Make a dictionary called cities . Use the names of three cities as keys in your dictionary . Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city . The keys for each city’s dictionary should be something like country, population, and fact . Print the name of each city and all of the infor- mation you have stored about it .
'''

cities = {
    'kathmandu':{
        'country':'nepal',
        'population':'3 million',
        'fact':'capital of its country',
    },
    'new delhi':{
        'country':'india',
        'population':'15 million',
        'fact':'most polluted city in the world',
    },
    'amsterdam':{
        'country':'netherlands',
        'population':'1 million',
        'fact':'where the large amouunt of people commute using bicycles'
    }
}

for city, city_info in cities.items():
    print(f"\n{city.title()} is in {city_info['country']} and has about {city_info['population']} and is {city_info['fact']}")