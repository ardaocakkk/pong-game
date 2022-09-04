from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_score()
        
    def update_score(self):
        self.goto(-120,280)
        self.write(f"Player-1: {self.l_score}",align="center",font={'Arial',50,'normal'})
        self.goto(120,280)
        self.write(f"Player-2: {self.r_score}",align="center",font={'Arial',50,'normal'})
        
        
    def increase_r_score(self):
        self.r_score +=1
        self.clear()
        self.update_score()
        
    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.update_score()
        
        