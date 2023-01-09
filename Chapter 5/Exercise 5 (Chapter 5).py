pets = []
pet = {
    'animal type': 'cat',
    'name': 'Dash',
    'owner': 'Sally',
    'weight': 20,
    'eats': 'tuna',
}
pets.append(pet)
 
pet = {
    'animal type': 'Hamster',
    'name': 'Chibby',
    'owner': 'Julie',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)
 
pet = {
    'animal type': 'dog',
    'name': 'Caramel',
    'owner': 'Elizah',
    'weight': 14,
    'eats': 'chicken',
}
pets.append(pet)
 
# Display information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")

#Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the
#owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about each pet