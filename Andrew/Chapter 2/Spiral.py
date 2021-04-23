# OvalSpirall.py
import turtle
t = turtle.Pen()
t.speed(7)

lineColors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
for x in range(100):
    t.forward(5*x)
    t.left(90)
    t.color(lineColors[x % len(lineColors)])
