import turtle
from math import pi

t = turtle.Turtle()

def polyline(t, n, lado, angulo):
    for i in range(n):
        t.fd(lado)
        t.lt(angulo)

def polygon (t, lado, n):
    angulo = 360 / n
    polyline (t, n, lado, angulo)

def arc(t, r, angulo):
    comprimento = 2 * pi * r * angulo / 360
    n = int(angulo / 4)
    lado = comprimento / n
    ang_parcial = float(angulo) / n
    polyline (t, n, lado, ang_parcial)

def circle(t, r):
    arc(t, r, 360)


arc(t, 100, 90)
turtle.done()
