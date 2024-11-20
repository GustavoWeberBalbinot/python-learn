import turtle
import math
bob = turtle.Turtle()

def espiral_arquimedes(bob,r,n):
    circumference_area = 2 * math.pi * r
    angle = 360 / n
    circumference_n_part = circumference_area / n
    for x in range(n * 10):
        bob.fd(r)
        bob.lt(angle)
        r += 1


espiral_arquimedes(bob, 10, 8)
turtle.mainloop()