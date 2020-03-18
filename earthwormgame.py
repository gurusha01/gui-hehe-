import os
import turtle
import time
import random
from tkinter import messagebox
#initialisation of the gamesetup
delay=0.2
wn=turtle.Screen()
wn.title("earthworm game")
wn.bgcolor("green")
wn.setup(width=500,height=500)
wn.tracer(0)
head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"
score=0
#ini food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)
segments=[]
def inc_tail():
    new_segment=turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("circle")
    new_segment.color("grey")
    new_segment.penup()
    segments.append(new_segment)
def move_snake():
    i=len(segments)-1
    for i in range (len(segments)-1, 0 , -1):
        segments[i].goto(segments[i-1].xcor(),segments[i-1].ycor())
    if len(segments)>0:
        segments[0].goto(head.xcor(),head.ycor())
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"
        
def move():
    if head.direction=="up":
         head.sety(head.ycor()+20)
    if head.direction=="down":
         head.sety(head.ycor()-20)
    if head.direction=="right":
         head.setx(head.xcor()+20)
    if head.direction=="left":
         head.setx(head.xcor()-20)     
wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_right,"Right")
wn.onkeypress(go_left,"Left")
while True:
    wn.update()
    time.sleep(delay)
    move()
    #collission with walls
    if head.xcor()<=-250 or head.ycor()<=-250 or head.xcor()>=250 or head.ycor()>=250:
        messagebox.showinfo("dead", score)
        wn.close()
    #collission with itself
    for segment in segments:
        if segment.distance(head)<20:
             messagebox.showinfo("dead", score)
             wn.destroy()
    if head.distance(food)<20:
        fx=random.randint(-200,200)
        fy=random.randint(-200,200)
        food.goto(fx,fy)#new food location
        inc_tail()#increase lail tength
        score=score+10
    move_snake()#moves the snake
wn.mainloop()
    
    
    
    
 
