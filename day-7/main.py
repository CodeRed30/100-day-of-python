import random

# Step 1
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
random_number = random.randint(0, len(word_list)-1)
chosen_word = word_list[random_number]

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Choose a letter: \n").lower()

print(chosen_word)
print(guess)

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


# TODO-1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []
for each in range(len(chosen_word)):
    display.append("_")

print(display)

# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

count = 0
for char in chosen_word:
    if guess == char:
        display[count] = guess
        count += 1
    else:
        count += 1

# TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

print(display)