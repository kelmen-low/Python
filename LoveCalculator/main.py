print("The Love Cauclator is calculating your score...")
name1 = input("Your name: ")
name2 = input("Their name: ")

combinedNames = name1 + name2
lowerNames = combinedNames.lower()

firstNumber = 0
secondNumber = 0

firstNumber += lowerNames.count("t")
firstNumber += lowerNames.count("r")
firstNumber += lowerNames.count("u")
firstNumber += lowerNames.count("e")

secondNumber += lowerNames.count("l")
secondNumber += lowerNames.count("o")
secondNumber += lowerNames.count("v")
secondNumber += lowerNames.count("e")

print(f"Your love score is: {firstNumber}{secondNumber}")