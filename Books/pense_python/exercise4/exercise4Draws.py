#quadrados (tortas de tartaruga)
import turtle

#quadrado 1:
def square1(bob,lenght):
    bob.lt(35)
    for x in range(0,6):
        bob.fd(lenght)
        bob.lt(121)
        bob.fd(lenght)
        bob.lt(119)
        bob.fd(lenght)
        bob.lt(180)
    turtle.mainloop()


#quadrado 2:

def square2(bob,lenght):
    bob.lt(90)
    for x in range(0,6):
        bob.fd(lenght)
        bob.lt(120)
        bob.fd(lenght)
        bob.lt(120)
        bob.fd(lenght)
        bob.lt(180)
    turtle.mainloop()

bob = turtle.Turtle()

square1(bob, 100)