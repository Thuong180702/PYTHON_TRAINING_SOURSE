import random

FullName = input("What is your full name?\n")

list_name = FullName.split(" ")
number_items = len(list_name)
random_choice = random.randint(0, number_items - 1)

print(list_name[random_choice])
