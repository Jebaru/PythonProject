# Day 5 Project👌

import random
# from typing import List

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# pass_letters = random.choices(letters, k=nr_letters)
# pass_symbols = random.choices(symbols, k=nr_symbols)
# pass_numbers = random.choices(numbers, k=nr_numbers)
#
# password = pass_letters + pass_symbols + pass_numbers

# Easy way
# password = ''
#
# for letter in range(0, nr_letters):
#     password += random.choice(letters)
# for symbol in range(0, nr_symbols):
#     password += random.choice(symbols)
# for num in range(0, nr_numbers):
#     password += random.choice(numbers)
#
# print(f"Here is your Password: {password}")

# Hard Way
# password_list = []
#
# for letter in range(0, nr_letters):
#     password_list.append(random.choice(letters))
# for symbol in range(0, nr_symbols):
#     password_list.append(random.choice(symbols))
# for num in range(0, nr_numbers):
#     password_list.append(random.choice(numbers))
#
# print(f"Here is your Password: {password_list}")
#
# random.shuffle(password_list)
# print(password_list)
#
# password = ""
# for i in password_list:
#     password += i
#
# print(password)

# Easy way of hard way
password = random.choices(letters, k=nr_letters) + random.choices(symbols, k=nr_symbols) + \
           random.choices(numbers, k=nr_numbers)
print(f"Before Shuffle: {password}")
random.shuffle(password)
password = ''.join(password)
print(f"After Shuffle: {password}")
