import time
from turtle import Screen
from player import FINISH_LINE_Y, STARTING_POSITION, Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_turtle, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    # Detect collision with cars
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            score.game_over()
    
    # Detect collision with wall
    if player.ycor() > FINISH_LINE_Y or player.ycor() < -FINISH_LINE_Y:
        player.goto(STARTING_POSITION)
        car.increase_speed()
        score.level_up()

screen.exitonclick()