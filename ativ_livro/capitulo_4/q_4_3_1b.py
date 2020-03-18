import turtle
dapaz = turtle.Turtle()

def square (t, lenght):
        for i in range(4):
            t.fd(lenght)
            t.lt(90)

square(dapaz, 100)
turtle.done()
