import turtle
import random

#first we need a screen and some configuration

win=turtle.Screen()
win.title('Pong Game')
win.setup(width=800,height=600)
win.bgcolor('black')
win.tracer(0)

#creating two paddles
paddle_a=turtle.Turtle()
paddle_b=turtle.Turtle()
ball=turtle.Turtle()


score_a=0
score_b=0


def paddleclass(paddle,shape,color,position):
	paddle.penup()
	paddle.speed(0)
	paddle.shape(shape)
	paddle.color(color)
	paddle.goto(position,0)
	paddle.shapesize(stretch_wid=5,stretch_len=1)

def ballclass(ball,shape,color,position):
	ball.penup()
	ball.speed(0)
	ball.shape(shape)
	ball.color(color)
	ball.goto(position,0)
	
#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


paddleclass(paddle_a,'square','white',-350)
paddleclass(paddle_b,"square","white",350)
ballclass(ball,'circle','white',0)

ball.dx=1
ball.dy=-1

#moving paddles
def paddle_a_up():
	y=paddle_a.ycor()
	y+=20
	paddle_a.sety(y)

def paddle_a_down():
	y=paddle_a.ycor()
	y-=20
	paddle_a.sety(y)

def paddle_b_up():
	y=paddle_b.ycor()
	y+=20
	paddle_b.sety(y)

def paddle_b_down():
	y=paddle_b.ycor()
	y-=20
	paddle_b.sety(y)


#keybindings for screen

win.listen()
win.onkeypress(paddle_a_up,'w')
win.onkeypress(paddle_a_down,'s')
win.onkeypress(paddle_b_up,'Up')
win.onkeypress(paddle_b_down,'Down')




#mainloop

while True:
	win.update()

#move the ball
	ball.setx(ball.xcor()+ball.dx)
	ball.sety(ball.ycor()+ball.dy)

	if ball.ycor()>290:
		ball.sety(290)
		ball.dy*=-1

	if ball.ycor()<-290:
		ball.sety(-290)
		ball.dy*=-1

	if ball.xcor()>390:
		ball.goto(0,0)
		ball.dx*=-1
		score_a=score_a+1
		pen.clear()
		pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))
		win.update()
	if ball.xcor()<-390:
		ball.goto(0,0)
		ball.dx*=-1
		score_b=score_b+1
		pen.clear()
		pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))
		win.update()
	#paddle and ball collision

	if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-40):
		ball.setx(340)
		ball.dx*=-1
	if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-40):
		ball.setx(-340)
		ball.dx*=-1
