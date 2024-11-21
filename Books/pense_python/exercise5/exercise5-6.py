import turtle
bob = turtle.Turtle()
bob.speed(10)

def koch(bob, length, depth):
    if depth == 0:
        bob.fd(length)
    else:
        length /= 3.0
        koch(bob, length, depth - 1)
        bob.lt(60)
        koch(bob,length, depth -1)
        bob.rt(120)
        koch(bob,length, depth -1)
        bob.lt(60)
        koch(bob, length, depth - 1)

def snowflake():
    for x in range(3):
        koch(bob,100,4)
        bob.rt(120)

snowflake()
turtle.mainloop()