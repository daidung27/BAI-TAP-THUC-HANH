print("TONG DOAN DAI DUNG")
print("msv:24575202161009")
import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")

painter = turtle.Turtle()
painter.color('blue')       
painter.pensize(3)      
painter.speed(0) 
window.tracer(False)    
def drawsq(t, s):
    """Vẽ một hình vuông với rùa t, độ dài cạnh s."""
    for i in range(4):
        t.forward(s)
        t.left(90)
for i in range(1, 180):
    painter.left(18)
    drawsq(painter, 200)

window.tracer(True) 
window.mainloop() 
