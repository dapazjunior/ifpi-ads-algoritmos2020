import turtle
bob = turtle.Turtle()

turtle.color('blue')
turtle.begin_fill()
for i in range(4):
    bob.fd(100)
    bob.lt(90)
turtle.end_fill()
turtle.done()
