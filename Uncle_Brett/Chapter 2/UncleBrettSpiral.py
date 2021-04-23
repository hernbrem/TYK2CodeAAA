# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 20:21:22 2021

@author: Brett
"""
import turtle
import math

def getXY(i):
    x = math.cos(0.1*i)*0.15*i
    y = math.sin(0.1*i)*0.3*i
    return x,y

def getColor(i):
    r = math.fabs(math.cos(0.1*i))
    g = math.fabs(math.sin(0.1*i))
    b = 0.5
    return (r,g,b)
                

t = turtle.Pen()

t.speed(0)
for i in range(1000):
    x, y = getXY(i)
    t.setposition(x,y)
    t.color(getColor(i))
    t.width(5)