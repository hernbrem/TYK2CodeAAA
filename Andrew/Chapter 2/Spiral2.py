# OvalSpiral2.py
import turtle
t = turtle.Pen()
t.speed(0)

lineColors = ['red', 'orange', 'black', 'green', 'blue', 'purple']
for x in range(200):
    t.forward(3*x)
    t.left(91)
    t.color(lineColors[x % len(lineColors)])
