# Ashton Haus
# CS30 Period 4
# May 6, 2020
# Rpg continuous game play


valid_actions = {"directions": ["north", "south", "east", "west"],
                 "actions": ["Quit", "Heal", "Attack", "Explore"]
                 }

while True:
    # print a list a valid actions before user input. Organized according to
    # possible direction and actions
    for user_action in valid_actions:
        if user_action == "actions":
            # prints out a list of valid actions from the list in valid_actions
            print(f"Complete one of the following {user_action}:")
            possible_actions = valid_actions["actions"]
            # using a loop, print out all the actions the user can use
            for action in possible_actions:
                print(f"* {action}")

    action_input = input("Action: ")
    direction = valid_actions["directions"]
    action = valid_actions["actions"]
    # convert the user input to all lower case to prevent errors
    # print out the action chosen
    if action_input == "quit":
        break

    elif action_input == "attack":
        print("You go attack!")
        print("--------------------------")
    elif action_input == "heal":
        print("You heal yourself!")
        print("--------------------------")
    elif action_input == "explore":
        print("You begin a journey ---------->")
        print(f"Go in one of the following directions:")
        # all the directions the user can go
        for d in direction:
            print(f"* {d}")
        direction_input = input("Which direction would you like to go?")
        if direction_input.lower() in direction:
            print(f"You begin travelling {direction_input}!")
        else:
            print("Invalid input. Try again.")
