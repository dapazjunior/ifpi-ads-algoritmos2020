import turtle
from math import pi

t = turtle.Turtle()

def polygon (t, lenght, n):
        for i in range(n):
            t.fd(lenght)
            t.lt(4)

def circle(t, r):
    lados = int(r/2 + 10)
    comprimento = r * pi * 2 / lados
    polygon(t, comprimento, lados)

def arc(t, r, angulo):
    comprimento = r * pi * 2 / 90
    lados = int(angulo / 4)
    polygon(t, comprimento, lados)


arc(t, 100, 360)
turtle.done()
