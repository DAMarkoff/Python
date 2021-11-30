import random
from turtle import Turtle

from config import CARS_COLOURS, SCREEN_HEIGHT, SCREEN_WIDTH, CAR_MOVE_INCREMENT, STARTING_MOVE_DISTANCE, CARS_NUMBERS


class Car(Turtle):
	
	def __init__(self):
		super().__init__()
		self.setheading(180)
		self.penup()
		self.shape('square')
		self.shapesize(1, 2)
		self.random_colour()
		self.random_position(from_right=False)
		self.distance_on_move = STARTING_MOVE_DISTANCE
	
	def random_colour(self):
		color = random.choice(CARS_COLOURS)
		self.color(color)
	
	def random_position(self, from_right):
		rand_x = random.randint(-SCREEN_WIDTH / 2, SCREEN_WIDTH / 2) if not from_right else SCREEN_WIDTH / 2 + 20
		rand_y = random.randint(-SCREEN_HEIGHT / 2 + 100, SCREEN_HEIGHT / 2 - 100)
		self.goto(rand_x, rand_y)
	
	def move(self):
		self.forward(self.distance_on_move)
	
	def move_faster(self):
		self.distance_on_move += CAR_MOVE_INCREMENT
		

class CarManager:
	
	def __init__(self):
		self.cars_list = []
		self.init_cars()
	
	def init_cars(self):
		for item in range(CARS_NUMBERS):
			car = Car()
			self.cars_list.append(car)
	
	def move(self):
		for car in self.cars_list:
			car.forward(car.distance_on_move)
			
	def move_faster(self):
		for car in self.cars_list:
			car.distance_on_move += CAR_MOVE_INCREMENT
		