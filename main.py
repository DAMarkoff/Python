import time
from turtle import Screen

from carmanager import CarManager
from config import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_FINISH_LINE_Y, CARS_NUMBERS
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

game_on = True

player = Player()
scoreboard = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkey(player.up, 'Up')

while game_on:
	time.sleep(0.1)
	screen.update()
	cars.move()
	
	for car in cars.cars_list:
		if car.xcor() < -SCREEN_WIDTH / 2:
			car.random_position(from_right=True)
		if car.distance(player) < 20:
			scoreboard.game_over()
			game_on = False

	if player.ycor() >= PLAYER_FINISH_LINE_Y:
		scoreboard.add_point()
		player.goto_on_start()
		cars.move_faster()

screen.exitonclick()
