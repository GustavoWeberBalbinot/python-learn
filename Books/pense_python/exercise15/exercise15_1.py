'''
Escreva uma definição para uma classe denominada Circle, com os atributos center e radius, onde center é um objeto Point e radius é um número.

Instancie um objeto Circle, que represente um círculo com o centro em 150, 100 e raio 75.

Escreva uma função denominada point_in_circle, que tome um Circle e um Point e retorne True, se o ponto estiver dentro ou no limite do círculo.

Escreva uma função chamada rect_in_circle, que tome um Circle e um Rectangle e retorne True, se o retângulo estiver totalmente dentro ou no limite do círculo.

Escreva uma função denominada rect_circle_overlap, que tome um Circle e um Rectangle e retorne True, se algum dos cantos do retângulo cair dentro do círculo. Ou, em uma versão mais desafiadora, retorne True se alguma parte do retângulo cair dentro do círculo.
'''

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

def point_in_circle(circle, rectangle):
    print('')

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

point_in_circle(cc,rg)