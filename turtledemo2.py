import turtle
a = turtle.Turtle()
a.showturtle()
a.pensize(2)
turtle.bgcolor("black")
a.speed(0)
for i in range(6):
    for colors in ["red","yellow","blue","cyan","magenta","green","white"]:
        a.color(colors)
        a.circle(100)
        a.left(10)

a.hideturtle()
turtle.mainloop()