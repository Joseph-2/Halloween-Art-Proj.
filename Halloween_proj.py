#imports
import turtle
import random
#import config
background = turtle.Screen()
background.setup(width=800,height=600)
background.bgpic("dribbble.gif")
background.addshape("gravestone.gif")
background.addshape("ghost.gif")
#variables
score = 0
time = 10
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#timer
timer = turtle.Turtle()
timer.hideturtle()
timer.penup()
timer.goto(-350,250)
timer.color("red")
timer.pendown()
#score count
score_count = turtle.Turtle()
score_count.hideturtle()
score_count.penup()
score_count.goto(350,250)
score_count.color("red")
score_count.pendown()
#ghost
ghost = turtle.Turtle()
ghost.penup()
ghost.hideturtle()
ghost.shape("ghost.gif")
ghost.turtlesize(.5)
#gravestone
gravestone = turtle.Turtle()
gravestone.shape("gravestone.gif")
gravestone.penup()
gravestone.goto(-300,-250)
#functions
def move_ghost():
  ghost.hideturtle()
  xcord = random.randint(-375,375)
  ycord = random.randint(-275,275)
  ghost.goto(xcord,ycord)
  ghost.showturtle()
def score_up():
  score_count.clear()
  global score
  score += 1
  score_count.write(score,font=("Arial",20,"bold"))
def gravestone_click(x,y):
  gravestone.hideturtle()
  ghost.showturtle()
def countdown():
  global time, timer_up, score
  timer.clear()
  if time <= 0:
    timer_up = True
    global score
    if score < 10:
      ghost.clear
      gravestone.clear
      timer.clear
      score_count.clear
      background.bgpic("68tz.gif")

    else:
      gravestone.clear()
      gravestone.color("red")
      gravestone.write("YOU WIN!", font=("Arial",50,"bold"))
  else:
    timer.write("Timer: " + str(time), font=("Arial",20,"bold"))
    time -= 1
    timer.getscreen().ontimer(countdown, counter_interval) 
def ghost_clicked(x,y):
  global timer_up
  if timer_up == False:
    score_up()
    ghost.hideturtle()
    xcord = random.randint(-375,375)
    ycord = random.randint(-275,275)
    ghost.goto(xcord,ycord)
    ghost.showturtle()
  else:
    ghost.hideturtle()
#events
gravestone.onclick(gravestone_click)
ghost.onclick(ghost_clicked)
background.ontimer(countdown, counter_interval)
background.mainloop() 