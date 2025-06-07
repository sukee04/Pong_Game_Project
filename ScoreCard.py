from turtle import Turtle

class ScoreCard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.score_update()
        

    def score_update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center',font=('courier', 30, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align='center',font=('courier', 30, 'normal'))

    def l_paddle_score(self):
        self.l_score += 1
        self.score_update()

    def r_paddle_score(self):
        self.r_score += 1
        self.score_update()