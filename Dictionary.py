# Ashton Haus
# CS30 Period 4
# March 12, 2020
# RPG Nested Dictionaries


def world(Name):
    # prints out the items, keys, and values in the dictionaries
    for Name, key in Name.items():
        # loops through the dictionaies and prints all the contents
        print(Name + ":")
        for items in key:
            # Goes through the nested dictionaries and prints the contents
            print(f"\t{items} - {key[items]}")

# the main character and his/hers stats
main_character = {"Main character": {
                  "Name": "Player",
                  "health": 10,
                  "attack": 3, }
                  }

# All the other characters in the game
side_characters = {"Side characters": {
                   "Grave robber": {"Roam around Cemetary, friend or enemy"},
                   "Homeless guy": {"Roam around back alley"},
                   "Bus driver": {"Possible friend or enemy"},
                   "Airport Security": {"Roams the airport, always an enemy"},
                   "Police": {"Roams around entire world, always have gun"}},
                   }
# Various locations within the world
locations = {"Locations": {
             "Bus stop": {"In sketchy neighbourhood, allows access to bus"},
             "Back alley": {"Dangerous, where the homeless roam"},
             "Cemetary": {"Dangerous, where the grave robbers roam"},
             "Store front": {"Access to store, can steal items "},
             "Airport": {"Access to plane, ending of the game"}},
             }

inventory = {"Inventory": {
             "Pistol": {"Total bullets left": 8},
             "Knife": {"Number of knives": 3},
             "Syringe": {"health item": "Used to heal 50% health"},
             "Bandages": {"health item": "Used to heal 25% health"},
             "MedKit": {"health item": "Used to heal 100% health"}},
             }

# Makes it easier to read
print("------------------------------------------------------------------")
# Prints out the main title for the dictionary
print("THE MAIN CHARACTER")
world(main_character)
# Makes it easier to read
print("------------------------------------------------------------------")
# Prints out the main title for the dictionary
print("THE SIDE CHARACTERS")
world(side_characters)
# Makes it easier to read
print("------------------------------------------------------------------")
# Prints out the main title for the dictionary
print("THE LOCATIONS")
world(locations)
# Makes it easier to read
print("------------------------------------------------------------------")
# Prints out the main title for the dictionary
print("THE INVENTORY")
world(inventory)
# Makes it easier to read
print("------------------------------------------------------------------")
