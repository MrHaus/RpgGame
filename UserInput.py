# Ashton Haus
# CS30 Period 4
# User Input

print("\nGo in one of the following directions:")
print("* 1 = forward")
print("* 2 = backward")

print("Complete one of the following actions:")
print("* 4 = Attack")
print("* 5 = Heal")
print("* 6 = Run Away")

decision = input("WHAT WILL YOU DO?(#)")
decision = int(decision)

if decision == 1:
    print("\nYou go forward!")
elif decision == 2:
    print("\nYou go backwards!")
elif decision == 4:
    print("\nYou Attack!")
elif decision == 5:
    print("\nYou Heal!")
elif decision == 6:
    print("\nYou run away like a coward!")
else:
    print("\nCommand Does Not Exist!")
print("------------------------------------------")
