'''
6-8. Pets: Make several dictionaries, where the name of each dictionary is the name of a pet . In each dictionary, include the kind of animal and the owner’s name . Store these dictionaries in a list called pets . Next, loop through your list and as you do print everything you know about each pet .
'''



pets = {
    'coco':{
        'name':'coco',
        'owner':'joe',
        'animalType':'dog'
    },

    'bronnie':{
        'name': 'bronnie',
        'owner':'kelly',
        'animalType':'cat'
    }
}

for pet_name, pet_info in pets.items():
    print(f"\n{pet_info['name'].title()} is a pet {pet_info['animalType']} owned by {pet_info['owner'].title()}")