import colorgram
import random
import turtle

list_color = colorgram.extract('image.jpg', 50)

def random_color():
    color_rgb = []
    for color in list_color:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        color_rgb.append(new_color)
    return random.choice(color_rgb)

alex = turtle.Turtle()
alex.speed('fastest')
alex.penup()
alex.hideturtle()
turtle.colormode(255)

alex.setheading(225)
alex.forward(300)
alex.setheading(0)

dot_numbers = 100
for dot_count in range(1, dot_numbers + 1):
    alex.dot(20, random_color())
    alex.forward(50)
    if dot_count % 10 == 0:
        alex.setheading(90)
        alex.forward(50)
        alex.setheading(180)
        alex.forward(500)
        alex.setheading(0)

screen = turtle.Screen()
screen.exitonclick()