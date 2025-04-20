'''
Escreva uma função chamada draw_rect que receba um objeto Turtle e um Rectangle e use o Turtle para desenhar o retângulo. Veja no Capítulo 4 os exemplos de uso de objetos Turtle.

Escreva uma função chamada draw_circle, que tome um Turtle e um Circle e desenhe o círculo.
'''

import turtle, math

tb = turtle.Turtle()


class Point():
    """Reference a point in x and y
    attributes: x, y
    """


class Rectangle():
    """Reference a rectangle
    attributes: width, height, corner
    """

rect = Rectangle()
rect.corner = Point()
rect.width = 150
rect.height = 80
rect.corner.x = 15
rect.corner.y = 27

class Circle():
    """Reference a circle
    attributes: center, radius
    """

cc = Circle()
cc.center = Point()
cc.radius = 20
cc.center.x = 15
cc.center.y = 15



def draw_rect(rc, t):
    points_rc = [
        (rc.corner.x, rc.corner.y),
        (rc.corner.x, rc.corner.y + rc.height),
        (rc.corner.x + rc.width, rc.corner.y + rc.height),
        (rc.corner.x + rc.width, rc.corner.y)
    ]
    t.penup()
    t.goto(points_rc[0])
    t.pendown()
    for x in points_rc:
        t.goto(x)
    t.goto(points_rc[0])
    t.penup()
    t.showturtle()
    turtle.mainloop()


def draw_circle(c, t):
    circumference = 2 * math.pi * c.radius
    segments = 100
    segments_lenght = circumference / segments
    angle = 360/ segments
    t.penup()
    t.goto(c.center.x - c.radius, c.center.y)
    t.pendown()
    for x in range(segments):
        t.fd(segments_lenght)
        t.lt(angle)
    turtle.mainloop()

draw_circle(cc, tb)