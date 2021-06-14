import turtle
import time
import random
from turtle import *
turtle.penup()
turtle.goto(-140,140)
turtle.speed(0)
for i in range(21):
    turtle.write(i, align="center")
    turtle.right(90)
    turtle.forward(10)
    turtle.pendown()
    turtle.forward(200)
    turtle.penup()
    turtle.backward(210)
    turtle.left(90)
    turtle.forward(20)

t1 = Turtle()
t1.color("lime green")
t1.shape("turtle")
t1.penup()
t1.goto(-160, 100)
t2 = Turtle()
t2.color("purple")
t2.shape("turtle")
t2.penup()
t2.goto(-160, 50)
t3 = Turtle()
t3.color("navy blue")
t3.shape("turtle")
t3.penup()
t3.goto(-160, 0)
t1.right(360)
t2.right(360)
t3.right(360)
for j in range(230):
    t1.forward(random.randint(1, 3))
    t2.forward(random.randint(1, 3))
    t3.forward(random.randint(1, 3))
    if t1.xcor() >= 270 or t2.xcor() >= 270 or t3.xcor() >= 270:
        turtle.goto(-140, 200)
        turtle.pensize(100)
        turtle.write("THE WINNER IS...", font=(0))
        time.sleep(2)
        if t1.xcor() > t2.xcor() and t1.xcor() > t3.xcor():
            t1.shapesize(10)
        elif t2.xcor() > t1.xcor() and t2.xcor() > t3.xcor():
            t2.shapesize(10)
        elif t3.xcor() > t2.xcor() and t3.xcor() > t1.xcor():
            t3.shapesize(10)
        turtle.done()

turtle.done()