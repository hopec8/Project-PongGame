from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.penup()
        self.goto(200, 230)
        self.write(arg=f"{self.score1}", align="center", font=("Arial", 50, "normal"))
        self.goto(-200, 230)
        self.write(arg=f"{self.score2}", align="center", font=("Arial", 50, "normal"))
        self.hideturtle()

    def increase_score1(self):
        self.score1 += 1
        self.clear()
        self.update_scoreboard()

    def increase_score2(self):
        self.score2 += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(200, 230)
        self.write(arg=f"{self.score1}", align="center", font=("Arial", 50, "normal"))
        self.goto(-200, 230)
        self.write(arg=f"{self.score2}", align="center", font=("Arial", 50, "normal"))



