from turtle import Turtle, Screen
import random

turtleColors = ["black", "blue", "green", "yellow", "red", "orange", "pink", "purple", "cyan", "dark blue"]


def randomDistance():
    return random.randint(0,30)

turtles = []

for i in range(10):
    t = Turtle()
    t.speed(0)
    t.color(turtleColors[i])
    t.shape("turtle")
    t.penup()
    t.setx(-600)
    t.sety((i * 120) - 600)
    turtles.append(t)


def startGame():

    stillGoing = True

    while stillGoing:
        for turtle in turtles:
            turtle.forward(randomDistance())
            if turtle.position()[0] >= 600:
                return turtle.fillcolor()
            else:
                continue


def checkAnswer(guess, actual):
    if guess.lower() == actual:
        print(f"You are correct! The {actual} turtle won!")
    else:
        print(f"You were wrong. The {actual} turtle won.")


s = Screen()
print(f"Here are the colors {turtleColors}")
colorGuess = s.textinput("Guess","Which color do you think will win? ")
winningColor = startGame()
checkAnswer(colorGuess,winningColor)

s.exitonclick()