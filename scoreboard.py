from turtle import Turtle

from init import screen

FONT = ('courier', 24, 'normal')


class Scoreboard(Turtle):
	
	def __init__(self):
		super().__init__()
		self.score = 50
		self.tries = 0
		self.hideturtle()
		self.penup()
		self.color('black')
		self.goto(-screen.window_width() /2 + 50, screen.window_height() / 2 - 50)
		self.refresh()
	
	def refresh(self):
		self.clear()
		self.write(f'Guessed States: {self.score}/50  Attempts: {self.tries}', align='left', font=FONT)
	
	def add_point(self):
		self.score -= 1
		self.refresh()