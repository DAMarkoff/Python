from turtle import Turtle

from config import SCREEN_HEIGHT, FONT, SCREEN_WIDTH


class Scoreboard(Turtle):
	
	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.penup()
		self.goto(-SCREEN_WIDTH / 2 + 80, SCREEN_HEIGHT / 2 - 40)
		self.level = 1
		self.refresh()
		
	def refresh(self):
		self.clear()
		self.write(f'Level: {self.level}', align='center', font=FONT)
		
	def add_point(self):
		self.level += 1
		self.refresh()
		
	def game_over(self):
		self.home()
		self.write('GAME OVER', align='center', font=FONT)