# Ashton Haus
# CS 30 Period 4
# February 24, 2020
# inventory for rpg game

# weapons list(empty)
weapons = []
# health items list(empty)
health = []

# you start off with zero weapons.
print(f"\nCurrent weapons:{weapons}")
# you start off with zero health items.
print(f"Current health items:{health}")
# separates each list method example.
print('-----------------------------------')

# prints out situation relating to append() method.
print(f'1.You find a bag containing weapons and health items!')
# adding knife to weapons list.
weapons.append('knife')
# adding gun to weapons list.
weapons.append('pistol')
# adding bandages to health items list.
health.append('bandages')
# adding syringe to health items list.
health.append('syringe')
# prints weapons added.
print(f"Current weapons:{weapons}")
# prints health items added.
print(f"Current health items:{health}")
# separates each list method example.
print('-----------------------------------')

# prints out situation relating to insert() method.
print(f'2.A medical kit falls from the sky and hits you!')
# prints current weapons.
print(f"Current weapons:{weapons}")
# inserting med kit in the beginning of list.
health.insert(0, 'med kit')
# prints health items list with med kit.
print(f"Current health items:{health}")
# separates each list method example.
print('-----------------------------------')

# prints out situation relating to del() method.
print(f'3.You realize your gun is fake so you throw it away!')
# gets rid of #1 in the list(gun).
del weapons[1]
# prints weapons list without gun.
print(f"Current weapons:{weapons}")
# prints health items list(not affected).
print(f"Current health items:{health}")
# separates each list method example.
print('-----------------------------------')

# creating a name for pop() function.
popped_health = health.pop()
# prints out situation relating to pop() method.
# prints the popped item using title() method.
print(f"4.A homeless guy steals your {popped_health.title()}!")
# prints weapons list.
print(f"Current weapons:{weapons}")
# prints health items list(without syringe).
print(f"Current health items:{health}")
# separates each list method example.
print('-----------------------------------')

# giving name for weapons item(knife).
attacked = 'knife'
# uses remove() method to get rid of knife.
weapons.remove(attacked)
# giving name for health item(syringe).
get_back = 'syringe'
# uses append() method to add syringe to list.
health.append(get_back)
# prints out situation relation to remove() method.
# prints the removed item with title() method.
print(f"5.You use your {attacked.title()} to get {get_back.title()} back!")
# prints weapons list(empty since knife is removed).
print(f"Current weapons:{weapons}")
# prints health items list(added syringe back).
print(f"Current health items:{health}")
# separates each list method example.
print('-----------------------------------')

# prints out situation relating to sorted() method.
print(f'6.You stop and organize your inventory!')
# prints out temperary sorted weapons list.
print(f"Current weapons:{sorted(weapons)}")
# prints out temperary sorted health items list.
print(f"Current health items:{sorted(health)}")
# separates each list method example.
print('-----------------------------------')

# prints out situation relating to sort() method.
print(f'7.You like how its organized so you leave it!')
# sorts weapons list permanently.
weapons.sort()
# prints sorted weapons list.
print(f"Current weapons:{weapons}")
# sorts health items list permanently.
health.sort()
# prints sorted health items list.
print(f"Current health items:{health}")
# separates each list method example.
print('-----------------------------------')

# prints out situation relating to len() method.
print(f'8.Airport security asks you how many items you are carrying!')
# prints out the number of items in each list using len().
print(f"I am carrying {len(weapons)} weapons and {len(health)} health items!")
# separates each list method example.
print('-----------------------------------')

# prints out sitaution relating to reverse() method.
print(f'9.The airport security went through your bag and reversed the order!')
# reverses the order of the weapons list permanently.
weapons.reverse()
# prints the weapons list in reverse.
print(f"Current weapons:{weapons}")
# reverses the order of the health items list permanently.
health.reverse()
# prints health items list in reverse.
print(f"Current health items:{health}")
# separates each list method example
print('-----------------------------------')
