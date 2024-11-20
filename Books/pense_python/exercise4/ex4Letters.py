import turtle
import math
bob = turtle.Turtle()

def mainloop():
    turtle.mainloop()

def draw_half_circle(r, direction):
    arc_length = 2 * math.pi * r * (180/ 360)
    y = int(arc_length/2) + 1
    segment_lenght = arc_length/y
    segment_angle = float(180)/y
    if direction == 'rt' :
        for x in range(y):
                bob.fd(segment_lenght)
                bob.rt(segment_angle)
    if direction == 'lt':
        for x in range(y):
                bob.fd(segment_lenght)
                bob.lt(segment_angle)

def goto_bob(x, y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def draw_a():
    bob.lt(60)
    bob.fd(100)
    bob.rt(120)
    bob.fd(100)
    bob.rt(180)
    bob.fd(50)
    bob.lt(60)
    bob.fd(50)
    mainloop()

def draw_b():
    bob.lt(90)
    bob.fd(100)
    bob.rt(90)
    for x in range(0,2):
        draw_half_circle(25, 'rt')
        bob.rt(180)
    mainloop()


def draw_c():
    bob.lt(180)
    draw_half_circle(50, 'rt')
    mainloop()


def draw_d():
     bob.lt(90)
     bob.fd(100)
     bob.rt(90)
     draw_half_circle(50, 'rt')
     mainloop()



def draw_e():
    for x in range(0,3):
        bob.fd(50)
        bob.rt(180)
        bob.fd(50)
        bob.rt(90)
        if x != 2:
            bob.fd(50)
            bob.rt(90)
    mainloop()

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
    mainloop()

def draw_g():
    bob.fd(25)
    bob.rt(90)
    bob.fd(45)
    bob.lt(270)
    draw_half_circle(65, 'rt')
    mainloop()

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
    mainloop()


def draw_i():
    bob.lt(90)
    bob.fd(80)
    bob.penup()
    bob.fd(10)
    bob.pendown()
    bob.fd(10)
    mainloop()


def draw_j():
    bob.rt(90)
    draw_half_circle(27, 'lt')
    bob.fd(75)
    bob.lt(90)
    bob.fd(50)
    bob.lt(180)
    bob.fd(100)
    mainloop()


def draw_k():
    bob.lt(90)
    bob.fd(100)
    bob.lt(180)
    bob.fd(50)
    bob.lt(135)
    bob.fd(70)
    bob.lt(180)
    bob.fd(70)
    bob.lt(90)
    bob.fd(70)
    mainloop()


def draw_l():
    bob.fd(50)
    bob.lt(180)
    bob.fd(50)
    bob.rt(90)
    bob.fd(100)
    mainloop()


def draw_m():
    bob.lt(60)
    bob.fd(100)
    bob.rt(120)
    bob.fd(40)
    bob.lt(120)
    bob.fd(40)
    bob.rt(120)
    bob.fd(100)
    mainloop()


def draw_n():
    bob.lt(60)
    bob.fd(100)
    bob.rt(130)
    bob.fd(100)
    bob.lt(140)
    bob.fd(100)
    mainloop()


def draw_p(key = 0):
    bob.lt(90)
    bob.fd(100)
    bob.rt(90)
    draw_half_circle(25, 'rt')
    if key == 0:
        mainloop()


def draw_q():
    bob.lt(180)
    draw_half_circle(25, 'rt')
    draw_half_circle(25, 'rt')
    bob.lt(180)
    bob.fd(20)
    bob.rt(35)
    bob.fd(20)
    bob.lt(180)
    bob.fd(40)
    mainloop()


def draw_r():
    draw_p(1)
    bob.lt(135)
    bob.fd(75)
    mainloop()


def draw_s():
    bob.fd(25)
    draw_half_circle(50,'lt')
    bob.fd(25)
    bob.rt(45)
    draw_half_circle(50,'rt')
    mainloop()


def draw_t():
    bob.lt(90)
    bob.fd(100)
    bob.lt(90)
    bob.fd(50)
    bob.lt(180)
    bob.fd(100)
    mainloop()


def draw_u():
    goto_bob(0,120)
    bob.rt(90)
    bob.fd(80)
    draw_half_circle(25,'lt')
    bob.fd(80)
    mainloop()


def draw_v(key = 0):
    goto_bob(-50,120)
    bob.rt(60)
    bob.fd(100)
    bob.lt(120)
    bob.fd(100)
    if key == 0:
        mainloop()


def draw_w():
    draw_v(1)
    bob.rt(120)
    bob.fd(100)
    bob.lt(120)
    bob.fd(100)
    mainloop()


def draw_x():
    bob.lt(45)
    bob.fd(100)
    goto_bob(75,0)
    bob.lt(90)
    bob.fd(100)
    mainloop()


def draw_y():
    bob.lt(60)
    bob.fd(100)
    goto_bob(0,90)
    bob.rt(120)
    bob.fd(60)
    mainloop()


def draw_z():
    goto_bob(0,100)
    bob.fd(100)
    bob.rt(135)
    bob.fd(120)
    bob.lt(135)
    bob.fd(100)
    mainloop()


