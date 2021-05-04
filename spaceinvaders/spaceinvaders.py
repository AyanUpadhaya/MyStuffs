import turtle
import os
import math
import random
import winsound

wn=turtle.Screen()#set up the screen
wn.title('Space invaders')
wn.bgpic('images/space.gif')
wn.bgcolor('black')
wn.setup(width=800,height=700)

#register the shapes

turtle.register_shape('images/invader2.gif') 
turtle.register_shape('images/spaceship2.gif')




#draw border

border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color('white')
border_pen.penup()
border_pen.setpos(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.ht()

#set the score to 0

score=0

#draw the score

score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-290,300)
scorestring="Score:%s "%(score)
score_pen.write(scorestring,False,align='left',font=('Arial',16,'normal'))
score_pen.ht()

#create player

player=turtle.Turtle()
player.color('blue')
player.shape('images/spaceship2.gif')
player.speed(0)
player.penup()
player.setposition(0,-250)
player.setheading(90)

playerspeed=15

enemyspeed=3

#choose the number of enemies
number_of_enemies=5

enemies=[]

for i in range(number_of_enemies):
	#create the enemy
	enemies.append(turtle.Turtle())

for enemy in enemies:
	enemy.color('red')
	enemy.shape('images/invader2.gif')
	enemy.penup()
	enemy.speed(0)
	x=random.randint(-200,200)
	y=random.randint(100,250)
	enemy.setposition(x,y)


#create bullet

bullet=turtle.Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed=20
#define bullet state

#ready-ready to fire
#fire- bullet

bulletstate="ready"

#Move the player left and right

def move_left():
	x=player.xcor()
	x-=playerspeed
	if x<-280:
		x=-280
	player.setx(x)

def move_right():
	x=player.xcor()
	x+=playerspeed
	if x>280:
		x=280
	player.setx(x)

def fire_bullet():
	#declare bullet state as global if it needs changed.
	global bulletstate
	if bulletstate=='ready':
		winsound.PlaySound('sounds/laser.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
		bulletstate='fire'
		#move the bullet
		x=player.xcor()
		y=player.ycor()+10
		bullet.setposition(x,y)
		bullet.showturtle()

def isCollision(t1,t2):
	distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance<15:
		return True
	else:
		return False



#keyboard binding

wn.listen()
wn.onkeypress(move_left,'Left')
wn.onkeypress(move_right,'Right')
wn.onkeypress(fire_bullet,'space')
#Main game loop
while True:
	wn.update()

	for enemy in enemies:

		#Move the enemy
		x=enemy.xcor()
		x+=enemyspeed
		enemy.setx(x)

		if enemy.xcor()>280:
			#Moves all enemies down
			for e in enemies:
				y=e.ycor()
				y-=40
				e.sety(y)
			#change direction
			enemyspeed*=-1
		if enemy.xcor()<-280:
			for e in enemies:
				y=e.ycor()
				y-=40
				e.sety(y)
			enemyspeed*=-1
		#check collision
		if isCollision(bullet,enemy):
			#reset the bullet
			winsound.PlaySound('sounds/explode.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
			bullet.hideturtle()
			bulletstate='ready'
			bullet.setposition(0,-400)
			#reset the enemy
			enemy.setposition(-200,250)

			score+=10
			scorestring+str(score)
			scorestring="Score:%s "%(score)
			score_pen.clear()
			score_pen.write(scorestring,False,align='left',font=('Arial',16,'normal'))
			score_pen.ht()


		if isCollision(player,enemy):
			winsound.PlaySound('sounds/explode.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
			player.hideturtle()
			enemy.hideturtle()
			print("Game Over")
			break

	#move the bullet
	if bulletstate=='fire':
		y=bullet.ycor()
		y+=bulletspeed
		bullet.sety(y)

	#check to if bullet has gone to top

	if bullet.ycor()>275:
		bullet.ht()
		bulletstate='ready'

	
