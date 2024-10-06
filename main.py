import random
from turtle import Turtle,Screen

timmyTheTurtle = Turtle()
timmyTheTurtle.shape("turtle")
timmyTheTurtle.color("blue")

#square
for _ in range(4):
    timmyTheTurtle.forward(100)
    timmyTheTurtle.right(90)
#dashed line
for _ in range(15):
    timmyTheTurtle.color("black")
    timmyTheTurtle.forward(10)
    timmyTheTurtle.penup()
    timmyTheTurtle.forward(10)
    timmyTheTurtle.pendown()

def draw_shape(num_sides):
#differnt shapes
  for _ in range(num_sides):
     angle = 360/num_sides
     timmyTheTurtle.forward(100)
     timmyTheTurtle.right(angle)

for shape_side_n in range(5,11):
    draw_shape(shape_side_n)

#draw a random walk
directions = [0,90,180,270]

for _ in range(200):

   timmyTheTurtle.backward(90)
   timmyTheTurtle.pensize(15)
   timmyTheTurtle.speed("fastest")
   timmyTheTurtle.setheading((random.choice(directions)))





screen = Screen()
screen.exitonclick()
