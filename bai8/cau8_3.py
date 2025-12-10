print("TONG DOAN DAI DUNG")
print("msv:24575202161009")
import turtle

colors = ["red","green","blue"]
painter = turtle.Turtle()
painter.pensize(3)
painter.speed(0)

for i in range(12):
    painter.pencolor(colors[i % 3])
    painter.circle(100)
    painter.right(30)

turtle.done()
