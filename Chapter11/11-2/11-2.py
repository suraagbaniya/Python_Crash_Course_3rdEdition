"""
11-2. Population: Modify your function so it requires a third parameter, population . It should now return a single string of the form City, Country – population xxx, such as Santiago, Chile – population 5000000 . Run test_cities.py again . Make sure test_city_country() fails this time .
Modify the function so the population parameter is optional . Run test_cities.py again, and make sure test_city_country() passes again .
Write a second test called test_city_country_population() that veri- fies you can call your function with the values 'santiago', 'chile', and 'population=5000000' . Run test_cities.py again, and make sure this new test passes .
"""

import unittest
from city_functions import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """ Test for neatly formatted city and country name. """
    
    def test_city_country(self):
        formatted_name = get_formatted_name('chitwan', 'nepal')
        self.assertEqual(formatted_name, "Chitwan, Nepal")
    
    def test_city_country_population(self):
        formatted_name = get_formatted_name('chitwan', 'nepal', 100000)
        self.assertEqual(formatted_name, "Chitwan, Nepal - population 100000")

unittest.main()