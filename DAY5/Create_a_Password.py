import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letter would you like in your password?: "))
nr_numbers = int(input("How many number would you like in your password?: "))
nr_symbols = int(input("How many symbol would you like in your password?: "))

password_list = []

for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

random.shuffle(password_list)
print(f"Your password is: {''.join(password_list)}")
