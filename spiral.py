import turtle

colors = ["red", "blue", "green", "gray", "orange", "black"]
a = turtle.Turtle()

for i in range(30):
    a.forward(20+i)
    a.left(30 - i/1.5)
    a.color(colors[i % 6])

turtle.done()
