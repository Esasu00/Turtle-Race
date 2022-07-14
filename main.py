import turtle
from random import randint
wn = turtle.Screen()
wn.bgcolor("cyan")

a = turtle.Turtle()
a.shape("turtle")
a.color("pink")
a.penup()
a.goto(-200,100)
a.pendown()

b = turtle.Turtle()
b.shape("turtle")
b.color("gray")
b.penup()
b.goto(-200,50)
b.pendown()

c = turtle.Turtle()
c.shape("turtle")
c.color("purple")
c.penup()
c.goto(-200,0)
c.pendown()


d = turtle.Turtle()
d.shape("turtle")
d.color("black")
d.penup()
d.goto(-200,-50)
d.pendown()

bob = turtle.Turtle()
bob.hideturtle()
bob.penup()
bob.goto(200,200)
bob.right(90)
bob.pendown()

bob.pensize(8)
bob.forward(500)


#Challenge: Race and Determine a winner
for turn in range(150):
  a.forward(randint(1,10))
  if a.xcor() >=200:
    print("PINK is the winner!")
    break
  b.forward(randint(1,10))
  if b.xcor() >=200:
    print("GRAY is the winner!")
    break
  c.forward(randint(1,10))
  if c.xcor() >=200:
    print("PURPLE is the winner!")
    break
  d.forward(randint(1,10))
  if d.xcor() >=200:
    print("BLACK is the winner!")
    break
