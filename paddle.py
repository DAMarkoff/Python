from turtle import Turtle

from config import PADDLE_STARTING_POSITIONS, PADDLE_SPEED


class Paddle(Turtle):

    def __init__(self, player_number):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.position = PADDLE_STARTING_POSITIONS[player_number]
        self.goto(self.position)
        self.setheading(90)
        self.distance_to_move = PADDLE_SPEED
        self.shapesize(stretch_len=5, stretch_wid=1)

    def move(self):
        self.forward(self.distance_to_move)

    def stop(self):
        self.distance_to_move = 0

    def up(self):
        # On key press paddle move version
        y_pos = self.ycor() + self.distance_to_move
        x_pos = self.position[0]
        self.goto(x_pos, y_pos)

        # Continuous paddle move version
        # if self.heading() == DOWN:
        #     self.setheading(UP)
        #     self.distance_to_move = PADDLE_SPEED

    def down(self):
        # On key press paddle move version
        y_pos = self.ycor() - self.distance_to_move
        x_pos = self.position[0]
        self.goto(x_pos, y_pos)

        # Continuous paddle move version
        # if self.heading() == UP:
        #     self.setheading(DOWN)
        #     self.distance_to_move = PADDLE_SPEED
