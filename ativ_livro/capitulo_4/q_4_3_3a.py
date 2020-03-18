import turtle
from math import pi

t = turtle.Turtle()

def polygon (t, lenght, n):
        for i in range(n):
            t.fd(lenght)
            t.lt(360/n)

def circle(t, r):
    # Comprimento da circunferência: c = 2 * pi * r
    # Perímetro do polígono: n(lados) * medida_do_lado
    # Comprimento da circunferência = Perímetro do polígono
    # 100 lados é adequado para o polígono parecer uma circunferência
    lados = int(r/2 + 10)
    comprimento = r * pi * 2 / lados
    polygon(t, comprimento, lados)

circle(t, 50)
turtle.done()
