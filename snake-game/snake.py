from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle()

        segment.penup()
        segment.color("white")
        segment.shape("square")
        segment.setposition(position)

        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):

        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() == DOWN:
            pass
        else:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() == UP:
            pass
        else:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() == RIGHT:
            pass
        else:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() == LEFT:
            pass
        else:
            self.head.setheading(RIGHT)
