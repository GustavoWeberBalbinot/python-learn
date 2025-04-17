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
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"({self.x}, {self.y})"

def point_in_circle(circle, point):
    euclidean_distance = math.sqrt(
        math.pow((point.x - circle.center.x),2) +  math.pow((point.y - circle.center.y),2)
        )
    if euclidean_distance <= circle.radius:
        return True
    return False


def rectangle_sides(rectangle):
    px_right = int(rectangle.corner.x + (rectangle.width/2))
    py_high= int(rectangle.corner.y + (rectangle.height/2))
    px_left = int(rectangle.corner.x - (rectangle.width/2))
    py_low = int(rectangle.corner.y - (rectangle.height/2))
    rectangle_points = [px_right,py_high], [px_right,py_low], [px_left,py_high], [px_left,py_low]
    return rectangle_points

def rect_in_circle(circle, rectangle, one_point = False):
    '''
    If point in rectangle there in the center
    '''
    count = 0
    rectangle_points=  rectangle_sides(rectangle)
    for x in rectangle_points:
        p = Point()
        p.x = x[0]
        p.y = x[1]
        if point_in_circle(circle,p):
            count += 1
            if one_point == True and count >= 1:
                print(f'The first side point {x[0]}x and {x[1]}y, there in the circle.')
                return True
    if count == 4:
        return True
    return False


def rect_circle_overlap(circle, rectangle, precision = 1):
    #I didnt use rectangle_sides function, because, this form is easier to understand
    px_right = int(rectangle.corner.x + (rectangle.width/2))
    py_high= int(rectangle.corner.y + (rectangle.height/2))
    px_left = int(rectangle.corner.x - (rectangle.width/2))
    py_low = int(rectangle.corner.y - (rectangle.height/2))
    high_width = list()
    lower_width = list()
    right_height = list()
    left_height = list()
    for x in range(px_left, px_right + 1, precision): #For the lower to high value in X
        po = Point()
        po.x = x
        po.y = py_high
        value = point_in_circle(circle,po)
        if value:
            if len(high_width) <= 1:
                high_width.append(po)
            else:
                high_width[1] = po
        po.y = py_low
        value = point_in_circle(circle,po)
        if value:
            if len(lower_width) <= 1:
                lower_width.append(po)
            else:
                lower_width[1] = po
    for y in range(py_low, py_high + 1, precision): #For the lower to high value in Y
        po = Point()
        po.x = px_right
        po.y = y
        value = point_in_circle(circle,po)
        if value:
            if len(right_height) <= 1:
                right_height.append(po)
            else:
                right_height[1] = po
        po.x = px_left
        value = point_in_circle(circle,po)
        if value:
            if len(left_height) <= 1:
                left_height.append(po)
            else:
                left_height[1] = po
    if len(high_width) >= 1:
        print(f'The high width:\nThe lower position is:{high_width[0]} and the Hight position is:{high_width[1]} cross the circle')
    if len(lower_width) >= 1:
        print(f'The high lower:\nThe lower position is:{lower_width[0]} and the Hight position is:{lower_width[1]} cross the circle')
    if len(right_height) >= 1:
        print(f'The right_height:\nThe lower position is:{right_height[0]} and the Hight position is:{right_height[1]} cross the circle')
    if len(left_height) >= 1:
        print(f'The left_height:\nThe lower position is:{left_height[0]} and the Hight position is:{left_height[1]} cross the circle')
        
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
rect_circle_overlap(cc, rg)
