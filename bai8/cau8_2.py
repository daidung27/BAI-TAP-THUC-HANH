print("TONG DOAN DAI DUNG")
print("msv:24575202161009")
import turtle
import random
import time 

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
colors = [
    "red", "green", "blue", "orange", 
    "purple", "pink", "yellow", "cyan", "magenta"]
painter = turtle.Turtle()
painter.shape("turtle") 
painter.speed(0) 
painter.pensize(3)
for i in range(10):
    color = random.choice(colors)
    painter.pencolor(color)
    painter.circle(100)
    painter.right(30)
    painter.left(60)
    painter.setposition(0, 0) 
screen.exitonclick()
