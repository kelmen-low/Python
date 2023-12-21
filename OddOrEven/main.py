def promptPlayAgain():
    answer = input("Do you want to play again? (y/n): ")
    if answer == "y":
        return True
    else:
        return False



playAgain = True

while playAgain:
    number = int(input("Enter an integer: "))
    if number % 2 == 0:
        print(f"{number} is even!")
        playAgain = promptPlayAgain()
    else:
        print(f"{number} is odd!")
        playAgain = promptPlayAgain()

