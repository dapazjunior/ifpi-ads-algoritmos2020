import turtle
dapaz = turtle.Turtle()

def polygon (t, lenght, n):
        for i in range(n):
            t.fd(lenght)
            t.lt(360/n)

polygon(dapaz, 150, 4)
turtle.done()
