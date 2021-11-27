from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 25, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.refresh()

    def refresh(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write(f'GAME OVER', move=False, align=ALIGNMENT, font=FONT)
