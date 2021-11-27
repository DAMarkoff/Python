import random
from random import randint
from turtle import Turtle

from config import BALL_DISTANCE_TO_MOVE, RIGHT, UP, LEFT, DOWN, BALL_SPEED_RATE, BALL_SPEED_DEFAULT, \
	BALL_DEVIATION_ON_BOUNCE_FROM_PADDLE, ANGLE_MIN, ANGLE_MAX


class Ball(Turtle):
	
	def __init__(self):
		super().__init__()
		self.shape('circle')
		self.penup()
		self.color('white')
		self.move_speed = BALL_SPEED_DEFAULT
		# self.shapesize(stretch_len=0.5, stretch_wid=0.5)
		self.random_heading = 0
		self.set_random_heading(heading='random')
		self.distance_to_move = BALL_DISTANCE_TO_MOVE
	
	def set_random_heading(self, heading):
		random_list = [randint(20, 50), randint(310, 340), randint(130, 160), randint(200, 230)]
		if heading == 'random':
			self.random_heading = random.choice(random_list)
		elif heading == 'left':
			self.random_heading = random.choice(random_list[2:])
		elif heading == 'right':
			self.random_heading = random.choice(random_list[:2])
		self.setheading(self.random_heading)
	
	def refresh(self, heading):
		self.home()
		self.move_speed = BALL_SPEED_DEFAULT
		self.set_random_heading(heading=heading)
	
	def move(self):
		self.forward(self.distance_to_move)
	
	def bounce_from_wall(self):
		self.setheading(360 - self.heading())
	
	def bounce_from_paddle(self, paddle_y):
		# Speed up a ball on bounce
		self.move_speed *= BALL_SPEED_RATE
		deviation, part = 0, ''
		# And bounce
		if RIGHT <= self.heading() < UP:
			if paddle_y - 30 < self.ycor() < paddle_y:
				part = 'down'
				if self.heading() > ANGLE_MIN:
					deviation += BALL_DEVIATION_ON_BOUNCE_FROM_PADDLE
			else:
				part = 'up'
				if self.heading() < ANGLE_MAX:
					deviation -= BALL_DEVIATION_ON_BOUNCE_FROM_PADDLE
			print(f'Sector: A, part: {part}, heading: {self.heading()}, dev: {deviation}')
			self.setheading((180 - self.heading()) + deviation)
		
		elif UP < self.heading() <= LEFT:
			if paddle_y - 30 < self.ycor() < paddle_y:
				part = 'down'
				if self.heading() < LEFT - ANGLE_MIN:
					deviation -= BALL_DEVIATION_ON_BOUNCE_FROM_PADDLE
			else:
				part = 'up'
				if self.heading() > LEFT - ANGLE_MAX:
					deviation += BALL_DEVIATION_ON_BOUNCE_FROM_PADDLE
			print(f'Sector: B, part: {part}, heading: {self.heading()}, dev: {deviation}')
			self.setheading(180 - self.heading() + deviation)
		
		elif LEFT < self.heading() < DOWN:
			deviation = 0
			if paddle_y - 30 < self.ycor() < paddle_y:
				part = 'down'
				if self.heading() < LEFT + ANGLE_MAX:
					deviation -= BALL_DEVIATION_ON_BOUNCE_FROM_PADDLE
			else:
				part = 'up'
				if self.heading() > LEFT + ANGLE_MIN:
					deviation += BALL_DEVIATION_ON_BOUNCE_FROM_PADDLE
			print(f'Sector: C, part: {part}, heading: {self.heading()}, dev: {deviation}')
			self.setheading(360 - (self.heading() - 180))
		
		elif DOWN < self.heading() < DOWN + UP:
			deviation = 0
			if paddle_y - 30 < self.ycor() < paddle_y:
				part = 'down'
				if self.heading() > DOWN + UP - ANGLE_MAX:
					deviation += BALL_DEVIATION_ON_BOUNCE_FROM_PADDLE
			else:
				part = 'up'
				if self.heading() < DOWN + UP - ANGLE_MIN:
					deviation -= BALL_DEVIATION_ON_BOUNCE_FROM_PADDLE
			print(f'Sector: D, part: {part}, heading: {self.heading()}, dev: {deviation}')
			self.setheading(270 - (self.heading() - 270))
