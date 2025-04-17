'''
Escreva uma definição para uma classe denominada Circle, com os atributos center e radius, onde center é um objeto Point e radius é um número.

Instancie um objeto Circle, que represente um círculo com o centro em 150, 100 e raio 75.

Escreva uma função denominada point_in_circle, que tome um Circle e um Point e retorne True, se o ponto estiver dentro ou no limite do círculo.

Escreva uma função chamada rect_in_circle, que tome um Circle e um Rectangle e retorne True, se o retângulo estiver totalmente dentro ou no limite do círculo.

Escreva uma função denominada rect_circle_overlap, que tome um Circle e um Rectangle e retorne True, se algum dos cantos do retângulo cair dentro do círculo. Ou, em uma versão mais desafiadora, retorne True se alguma parte do retângulo cair dentro do círculo.
'''

import math

class Circle():
    """Is a reference to a Circle
    attributes: center, radius
    """

class Rectangle():
    """Reference a Rectangle
    attributes: width, height, corner
    """

class Point():
    """Reference a point
    attributes: x, y
    """

def point_in_circle(circle, point):
    euclidean_distance = math.sqrt(
        math.pow((point.x - circle.center.x),2) +  math.pow((point.y - circle.center.y),2)
        )
    if euclidean_distance <= circle.radius:
        print(f'The point, {point.x}x and {point.y}y, there in the circle.')
    else:
        print(f'The point, {point.x}x and {point.y}y, not there in the circle.')
    return True


def rect_in_circle(circle, rectangle):
    '''
    If point in rectangle there in the center
    '''
    count = 0
    rectangle.point = Point()
    px_right = rectangle.corner.x + (rectangle.width/2)
    py_right= rectangle.corner.y + (rectangle.height/2)
    px_left = rectangle.corner.x - (rectangle.width/2)
    py_left = rectangle.corner.y - (rectangle.height/2)
    rectangle_points = [px_right,py_right], [px_right,py_left], [px_left,py_right], [px_left,py_left]
    for x in rectangle_points:
        p = Point()
        p.x = x[0]
        p.y = x[1]
        if point_in_circle(circle,p):
            count += 1
    if count == 4:
        return True
    return False


cc = Circle()
cc.center = Point()
cc.center.x = 150
cc.center.y = 100
cc.radius = 75

rg = Rectangle()
rg.corner = Point()
rg.width = 100
rg.height = 100
rg.corner.x = 50
rg.corner.y = 50

p = Point()
p.x = 74
p.y = 100

#value = point_in_circle(cc,p)
#print(value)
print(rect_in_circle(cc, rg))