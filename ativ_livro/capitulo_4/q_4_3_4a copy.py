import turtle
from math import pi

t = turtle.Turtle()

def arc(t, r, angulo):
    comprimento = r * pi * 2 * angulo / 360
    n = int(comprimento / 3) + 1
    comprimento_arco = comprimento / n
    angulo_arco = angulo / n
    for i in range(n):
        t.fd(comprimento_arco)
        t.lt(angulo)

def polyline(t, n, lenght, angulo):
    for i in range(n):
        t.fd(lenght)
        t.lt(angulo)

polyline(t, 100, 100, 30)
turtle.done()
