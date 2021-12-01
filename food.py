import random
from turtle import Turtle

from config import SCREEN_WIDTH, SCREEN_HEIGHT


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randint(-SCREEN_WIDTH / 2 + 20, SCREEN_WIDTH / 2 - 20)
        random_y = random.randint(-SCREEN_HEIGHT / 2 + 20, SCREEN_HEIGHT / 2 - 40)
        self.goto(random_x, random_y)
