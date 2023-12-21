print("Welcome to Python Pizza")

size = input("What size pizza would you like? (S/M/L): ")
totalBill = 0

if size == "S":
    totalBill += 15
elif size == "M":
    totalBill += 20
else:
    totalBill += 25

peperoni = input("Would you like to add peperoni? (y/n): ") == "y"

if peperoni & (size == "S"):
    totalBill += 2
if peperoni & (size != "S"):
    totalBill += 3

cheese = input("Would you like to add extra cheese? (y/n): ") == "y"

if cheese:
    totalBill += 1

print(f"Your total comes to {totalBill}")