import turtle
import time

player_a_name = input("Joueur 1 : ")

player_b_name = input("Joueur 2 : ") 

window = turtle.Screen()# open a window
window.title("Py Pong")# the title of the window
window.bgcolor("black")# the backround color of the window
window.setup(width=800, height=600)# the size of the window
window.tracer(0)#speeds up the game

#Score

score_a = 0
score_b = 0 

# Paddle A
paddle_a = turtle.Turtle()#the paddle a
paddle_a.speed(0)# the animation speed of the paddle
paddle_a.shape("square")# the shape of the paddle
paddle_a.color("white")# the color of the paddle
paddle_a.shapesize(stretch_wid=5, stretch_len=1)# controls the sqware size 
paddle_a.penup()# stops make the paddle
paddle_a.goto(-350, 0)# sets the paddle starting possision

# Paddle B
paddle_b = turtle.Turtle()#the paddle b
paddle_b.speed(0)# the animation speed of the paddle
paddle_b.shape("square")# the shape of the paddle
paddle_b.color("white")# the color of the paddle
paddle_b.shapesize(stretch_wid=5, stretch_len=1)# controls the sqware size 
paddle_b.penup()# stops make the paddle
paddle_b.goto(350, 0)# sets the paddle starting possision

# Ball
ball = turtle.Turtle()#the ball
ball.speed(0)# the animation speed of the ball
ball.shape("square")# the shape of the ball
ball.color("white")# the color of the ball
ball.penup()# stops make the ball
ball.goto(0, 0)# sets the ball starting possision
ball.dx = 0.3 # sets how much x pixels the ball moves
ball.dy = 0.3 # sets how much y pixels the ball moves

# Pen
pen = turtle.Turtle()# sets the Turtle to the pen
pen.speed(0)# sets the pen animation speed
pen.color("white")# sets the color of the pen to white
pen.penup()#it stos whriting
pen.hideturtle()# hides the pen turtle
pen.goto(0, 260)#we set the place we want to write
pen.write(player_a_name+": "+str(score_a)+"    "+player_b_name+": "+str(score_b), align="center", font=("Courier", 24, "normal"))#there we chose the thing we want to write the font the type oan the size of the leters


#Function
def paddle_a_up():
    y = paddle_a.ycor()#finds the paddle pos and set it to the y
    y += 20# add 20 pixels to y 
    paddle_a.sety(y)#sets the y ass the paddle pos

def paddle_a_down():
    y = paddle_a.ycor()#finds the paddle pos and set it to the y
    y -= 20# subtrack 20 pixels to y 
    paddle_a.sety(y)#sets the y ass the paddle pos

def paddle_b_up():
    y = paddle_b.ycor()#finds the paddle pos and set it to the y
    y += 20# add 20 pixels to y 
    paddle_b.sety(y)#sets the y ass the paddle pos

def paddle_b_down():
    y = paddle_b.ycor()#finds the paddle pos and set it to the y
    y -= 20# subtrack 20 pixels to y 
    paddle_b.sety(y)#sets the y ass the paddle pos


#Keyboard binding

window.listen()# makes the program whats out for keys to press
window.onkeypress(paddle_a_up, "z")# when the key w press the program take the paddle_a_up function and run it
window.onkeypress(paddle_a_down, "s")# when the key s press the program take the paddle_a_down function and run it
window.onkeypress(paddle_b_up, "Up")# when the key up press the program take the paddle_a_up function and run it
window.onkeypress(paddle_b_down, "Down")# when the key down press the program take the paddle_a_down function and run it

# main game loop
while True:

    if score_a == 3:
        turtle.Screen().bye()
        print(player_a_name+" A Gagné La Partie!!!")
        time.sleep(1000)
    if score_b == 3:
        turtle.Screen().bye()
        print(player_b_name+" A Gagné La Partie!!!")
        time.sleep(1000)


        
    window.update()# updates the game window

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)#moves the ball to the x
    ball.sety(ball.ycor() + ball.dy)#moves the ball to the y

    # Border checking
    if ball.ycor() > 290: #says if the ball y was above 290
        ball.sety(290)# set the ball y pos to 290
        ball.dy *= -1# revers the direction of the ball
        
    if ball.ycor() < -290: #says if the ball y was down of -290
        ball.sety(-290)# set the ball y pos to -290
        ball.dy *= -1# revers the direction of the ball

    if ball.xcor() > 390: #it says if the ball go to x 390
        ball.goto(0, 0)# ge the ball back to 0 0
        ball.dx *= -1 #chanhe the ball direction
        score_a += 1 # adds 1 point to the payer a
        pen.clear()# there we clear the score to have space to white the new
        pen.write(player_a_name+": "+str(score_a)+"    "+player_b_name+": "+str(score_b), align="center", font=("Courier", 24, "normal"))#prints the new score on the screen

    if ball.xcor() < -390: #it says if the ball go to x -390
        ball.goto(0, 0)# ge the ball back to 0 0
        ball.dx *= -1 #chanhe the ball direction
        score_b += 1 # adds 1 point to the payer b
        pen.clear()# there we clear the score to have space to white the new
        pen.write(player_a_name+": "+str(score_a)+"    "+player_b_name+": "+str(score_b), align="center", font=("Courier", 24, "normal"))#prints the new score on the screen

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):# it says if the x pos is biger than 340 and less than 350 and is in a radius of 80 to paddle
        ball.setx(340)# reverse the direction
        ball.dx *= -1 # change the direction of the ball

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):# it says if the x pos is smaler than -340 and more than -350 and is in a radius of 80 to paddle
        ball.setx(-340)# reverse the direction
        ball.dx *= -1 # change the direction of the ball

        
