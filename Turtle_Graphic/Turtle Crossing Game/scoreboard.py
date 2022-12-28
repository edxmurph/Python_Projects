from turtle import Turtle

FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", font = FONT)
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align = 'center', font = FONT)