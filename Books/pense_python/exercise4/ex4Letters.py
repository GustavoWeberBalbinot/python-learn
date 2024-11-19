import turtle
import math
bob = turtle.Turtle()

def draw_half_circle(r):
    arc_length = 2 * math.pi * r * (180/ 360)
    y = int(arc_length/2) + 1
    segment_lenght = arc_length/y
    segment_angle = float(180)/y
    for x in range(y):
            bob.fd(segment_lenght)
            bob.rt(segment_angle)

def draw_a():
    bob.lt(60)
    bob.fd(100)
    bob.rt(120)
    bob.fd(100)
    bob.rt(180)
    bob.fd(50)
    bob.lt(60)
    bob.fd(50)


def draw_b():
    bob.lt(90)
    bob.fd(100)
    bob.rt(90)
    for x in range(0,2):
        draw_half_circle(25)
        bob.rt(180)

def draw_c():
    bob.lt(180)
    draw_half_circle(50)


def draw_d():
     bob.lt(90)
     bob.fd(100)
     bob.rt(90)
     draw_half_circle(50)



def draw_e():
    for x in range(0,3):
        bob.fd(50)
        bob.rt(180)
        bob.fd(50)
        bob.rt(90)
        if x != 2:
            bob.fd(50)
            bob.rt(90)

def draw_f():
    bob.lt(90)
    bob.fd(50)
    bob.rt(90)
    for x in range(0,2):
        bob.fd(50)
        bob.rt(180)
        bob.fd(50)
        bob.rt(90)
        if x != 1:
            bob.fd(50)
            bob.rt(90)

def draw_g():
    bob.fd(25)
    bob.rt(90)
    bob.fd(45)
    bob.lt(270)
    draw_half_circle(65)

def draw_h():
    bob.lt(90)
    bob.fd(100)
    bob.lt(180)
    bob.fd(50)
    bob.lt(90)
    bob.fd(50)
    bob.rt(90)
    bob.fd(50)
    bob.rt(180)
    bob.fd(100)



draw_h()
turtle.mainloop()