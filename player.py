from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        # global STARTING_POSITION
        self.goto(STARTING_POSITION)

    def move_turtle(self):
        # global MOVE_DISTANCE  
        new_Y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_Y)