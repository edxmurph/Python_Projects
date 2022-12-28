from turtle import Turtle

class NameStates(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
    
    def show_up(self, position, name_state):
        self.goto(position)
        self.write(f"{name_state}", align = "center", font = ("Courier", 10, "bold"))