from turtle import Turtle, Screen
import random

screen  = Screen()
screen.setup(width = 500, height = 500)

colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
user_bet = ''
while user_bet not in colors:
    user_bet = screen.textinput(title = 'Make your bet', prompt = 'Which turtle will win the race? Enter a color: ')

turtles = []
y = 120
for color in colors:
    new_turtle = Turtle('turtle')
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-240, y)
    turtles.append(new_turtle)
    y -= 50

is_race_on = False
if user_bet:
    is_race_on = True

winning_color = []
while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() >= 220:
            is_race_on = False
            winning_color.append(turtle.pencolor())
            if user_bet in winning_color:
                print(f"You've won. The {user_bet} turtle is the winner!")
            else:
                for color in  winning_color:
                    print(f"You've lost. The {color} turtle is the winner!")

screen.exitonclick()
