from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.right_score, align='center', font=('Courier', 80, 'normal'))

    def left_point(self):
        self.left_score += 1
        self.update()
        
    def right_point(self):
        self.right_score += 1
        self.update()

    def game_over(self):
        winner = 'LEFT' if self.left_score > self.right_score else 'RIGHT'
        self.goto(0, 10)
        self.write('GAME OVER', align='center', font=('Courier', 60, 'normal'))
        self.goto(0, -20)
        self.write(f'{winner} PLAYER WINS', align='center', font=('Courier', 40, 'normal'))
