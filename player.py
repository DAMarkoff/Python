from turtle import Turtle

from config import SCREEN_HEIGHT, PLAYER_MOVE_DISTANCE


class Player(Turtle):
	
	def __init__(self):
		super().__init__()
		self.shape('turtle')
		self.color('green')
		self.setheading(90)
		self.penup()
		self.goto(0, -SCREEN_HEIGHT / 2 + 40)
		
	def up(self):
		self.forward(PLAYER_MOVE_DISTANCE)
	
	def goto_on_start(self):
		self.goto(0, -SCREEN_HEIGHT / 2 + 40)
		