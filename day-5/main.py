import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Easy
# print("Welcome to the PyPassword Generator")

# letters_req = int(input("How many letters would you like in your password?\n"))
# symbols_req = int(input("How many symbols would you like in your password?\n"))
# numbers_req = int(input("How many numbers would you like in your password?\n"))

# password = ""

# for letter in range(0, letters_req):
#     password += random.choice(letters)

# for symbol in range(0, symbols_req):
#     password += random.choice(symbols)

# for number in range(0, numbers_req):
#     password += random.choice(numbers)

# print(f"Here is your {password}")

# Hard
print("Welcome to the PyPassword Generator")

letters_req = int(input("How many letters would you like in your password?\n"))
symbols_req = int(input("How many symbols would you like in your password?\n"))
numbers_req = int(input("How many numbers would you like in your password?\n"))

password_list = []
password = ""

for letter in range(0, letters_req):
    password_list += random.choice(letters)

for symbol in range(0, symbols_req):
    password_list += random.choice(symbols)

for number in range(0, numbers_req):
    password_list += random.choice(numbers)

random.shuffle(password_list)

for character in password_list:
    password += character

print(f"Here is your {password}")
