#imports
import turtle
import random
#variables

#import config
background = turtle.Screen()
gravestone = turtle.Turtle()
background.setup(width=800,height=600)
background.bgpic("dribbble.gif")
background.addshape("gravestone.gif")
gravestone.shape("gravestone.gif")
gravestone.penup()
gravestone.goto(-300,-250)
#functions

#events
background.mainloop() 