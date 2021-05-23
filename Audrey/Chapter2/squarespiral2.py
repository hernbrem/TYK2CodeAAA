#squarespiral2.py
import turtle
t = turtle.Pen()
t.speed(0)
colors = ["red", "orange", "yellow", "green", "blue", "purple", "hot pink"]
for x in range(1000):
    t.width(10)
    t.pencolor( colors[ x % 7] )
    t.forward(x*2)
    t.left(100)
