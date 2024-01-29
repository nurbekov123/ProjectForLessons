import turtle

pen = turtle.Turtle()
okno = turtle.Screen()

def dom(x,y):
    pen.up()
    pen.goto(x,y)
    pen.down()

#квадрат
pen.begin_fill()
pen.fillcolor('blue')
dom(-120,-100)
pen.forward(240)
pen.left(90)
pen.forward(260)
pen.left(90)
pen.forward(240)
pen.left(90)
pen.forward(260)
pen.end_fill()

#крыша
pen.begin_fill()
pen.fillcolor('green')
dom(-200,160)
pen.goto(200,160)
pen.goto(0,280)
pen.goto(-200,160)
pen.end_fill()

#окно
pen.begin_fill()
pen.fillcolor('white')
dom(-60,45)
pen.left(90)
pen.circle(50)
pen.end_fill()

pen.pensize(2)
pen.color('yellow')
pen.left(90)
pen.forward(100)
pen.forward(-50)
pen.right(90)
pen.forward(50)
pen.forward(-100)

#дверь
pen.color('black')
pen.begin_fill()
pen.fillcolor('brown')
dom(40,-100)
pen.forward(60)
pen.left(90)
pen.forward(150)
pen.left(90)
pen.forward(60)
pen.left(90)
pen.forward(150)
pen.end_fill()

okno.mainloop()