import turtle

def Pattern(l=1 ):
    for x in range(360):
        t.pencolor(colors[x % 6])
        t.width(x / 100 + 1)
        t.forward(x*l)
        t.right(59)


screen=turtle.Screen()
screen.tracer(0)
t=turtle.Pen()
turtle.speed(10)
turtle.delay(0)
turtle.bgcolor('black')
t.hideturtle()
colors=['red','purple','blue','green','yellow','orange']
l=0.5
v=0.04
for g    in range(10000):
    t.clear()
    Pattern(l)
    screen.update()
    t.home()
    t.right(g)
    l=l+v
    if (l>10 or l<0.1):
        v=-v


turtle.exitonclick()