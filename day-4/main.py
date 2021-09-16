import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


player = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors?\n")
)

display_image = [rock, paper, scissors]
computer = random.randint(0, 2)

player_rock = ["Its a draw!", "You lose!", "You win!"]
player_paper = ["You win!", "You draw!", "You lose!"]
player_scissors = ["You lose!", "You win!", "You draw!"]

master_answers = [player_rock, player_paper, player_scissors]

if player > 2 or player < 0:
    print("Invalid answer, try again!")
else:
    print("You chose: \n")
    print(display_image[player])
    print("\nComuter chose: \n")
    print(display_image[computer])
    print(master_answers[player][computer])

print("The End!")
