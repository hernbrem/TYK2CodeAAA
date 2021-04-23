# CircleSpiral1.py
import turtle
t = turtle.Pen()
t.speed(0)

lineColors = ['red', 'orange', 'black', 'green', 'blue', 'purple']
for x in range(300):
    t.circle(x)
    t.left(6.5)
    t.color(lineColors[x % len(lineColors)])
