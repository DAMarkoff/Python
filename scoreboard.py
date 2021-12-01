from turtle import Turtle

from config import SCORE_ALIGNMENT, SCORE_FONT, SCORE_POSITION


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        with open('high_score.txt') as file:
            self.high_score = int(file.read())
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(SCORE_POSITION)
        self.refresh()

    def refresh(self):
        self.score += 1
        self.clear()
        # self.goto(SCORE_POSITION)  # write Game Over and offer a new game
        self.write(f'Score: {self.score}  High score: {self.high_score}', move=False, align=SCORE_ALIGNMENT, font=SCORE_FONT)

    def game_over(self):
        self.home()
        self.write(f'GAME OVER', move=False, align=SCORE_ALIGNMENT, font=SCORE_FONT)
    
    def reset(self):
        # self.game_over()  # write Game Over and offer a new game
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode='w') as file:
                file.write(str(self.high_score))
        self.score = -1
        self.refresh()
        