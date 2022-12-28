import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
carmanager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_car()
    carmanager.move()

    if player.ycor() > 280:
        player.refresh()
        scoreboard.update()
        carmanager.speed_up()
    for car in carmanager.cars:
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()