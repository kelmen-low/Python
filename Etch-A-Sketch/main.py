from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def moveForward():
    t.forward(10)


def moveBackward():
    t.back(15)


def turnRight():
    t.right(5)


def turnLeft():
    t.left(5)


def clear():
    t.clear()

screen.listen()
screen.onkey(moveForward, "w")
screen.onkey(moveBackward, "s")
screen.onkey(turnRight, "d")
screen.onkey(turnLeft, "a")
screen.onkey(clear, "c")
screen.exitonclick()
