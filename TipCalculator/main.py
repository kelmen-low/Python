# Welcome statement
print("Welcome to the tip calculator")

# Asking for the total bill
total = float(input("Please provide the total of the bill: "))

# Asking for the percentage tip
percent = float(input("What percentage tip would you like to give?: "))

# calculate how much the percentage is
total += (total * (percent / 100))

# Ask how many people to split the bill by
numberOfPeople = int(input("How many people would you like to split the bill by?: "))

# Output the final answer
print(f"Each person should pay {round(total / numberOfPeople,2)}")
