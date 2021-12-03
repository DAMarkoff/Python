from turtle import Turtle


class Dot(Turtle):
	
	def __init__(self):
		super().__init__()
		self.penup()
		self.color('red')
		self.shape('circle')
		
	def move(self, name, x, y):
		self.goto(x, y)
		self.write(f'{name}', align='center', font=('courier', 16, 'bold'))
		self.hideturtle()
		