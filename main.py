import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

generate_new_car = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    if generate_new_car == 6:
        car_manager.create_car()
        generate_new_car = 0
    else:
        generate_new_car += 1
    car_manager.move_cars()
    screen.update()

    for cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            # hit
            game_is_on = False

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


scoreboard.game_over()
screen.exitonclick()
