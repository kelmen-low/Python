import random

namesString = input("Names (X, X...): ")

names = namesString.split(", ")

randomChoice = random.randint(0, len(names) - 1)

print(f"{names[randomChoice]} was selected")