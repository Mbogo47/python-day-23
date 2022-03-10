from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-280, 260)
        self.write(f"Level:{self.level}", align="left", font= FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level:{self.level}", align="left", font= FONT)

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.goto(0,0)
        self.write("Game Over", align="left", font= FONT)