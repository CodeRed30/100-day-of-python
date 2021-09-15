print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
choice_1 = input("So what will it be, left or right?\n")
if choice_1.lower() == "left":
    choice_2 = input(
        "You have reached a moat, what will you do, swim or wait?\n")
    if choice_2.lower() == "wait":
        choice_3 = input(
            "You turn around and see three doors behind you, which one will you choose? Blue, Red or Yellow?\n")
        if choice_3.lower() == "red":
            print("Burned by fire. Game Over!")
        elif choice_3.lower() == "blue":
            print("Eaten by beasts. Game Over!")
        elif choice_3.lower() == "yellow":
            print("You win!")
        else:
            print("Game Over!")
    else:
        print("You were attacked by a trout. Game Over")
else:
    print("Fall into a hole. Game Over")
