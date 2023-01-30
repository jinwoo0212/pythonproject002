import turtle as t
import random
import time
  
        
t.bgcolor("lightgreen")
t.setup(500,700)

#플레이어(ball)
ball=t.Turtle()
ball.shape("circle")
ball.shapesize(1.1)
ball.up()
ball.speed(0)
ball.color("white")
ball.goto(-190,-135)

#길
way=t.Turtle()
way.shape("square")
way.shapesize(1,20)
way.up()
way.speed(0)
way.goto(0,-270)

#스테이지 통과
star=t.Turtle()
star.shape("turtle")
star.shapesize(2.2)
star.up()
star.speed(0)
star.color("yellow")
star.goto(190,-135)


