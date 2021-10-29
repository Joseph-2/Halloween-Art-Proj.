#imports
import turtle
import random
#import config
background = turtle.Screen()
background.setup(width=800,height=600)
background.bgpic("dribbble.gif")
background.addshape("gravestone.gif")
background.addshape("ghost.gif")
#ghost
ghost = turtle.Turtle()
ghost.penup()
ghost.hideturtle()
ghost.shape("ghost.gif")
#gravestone
gravestone = turtle.Turtle()
gravestone.shape("gravestone.gif")
gravestone.penup()
gravestone.goto(-300,-250)
#functions
def move_ghost():
  xcord = random.randint(-375,375)
  ycord = random.randint(-275,275)
  ghost.goto(xcord,ycord)
def score_up():
  pass
#events
background.mainloop() 