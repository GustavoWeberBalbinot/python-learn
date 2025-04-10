'''
Como exercício, escreva uma versão de move_rectangle que cria e retorne um novo retângulo em vez de alterar o antigo.
'''

import copy

class Rectangle():
    """Rectangle
    attributes: width, height, corner
    """

class Point():
    """Point
    attributes: x,y
    """


def move_rectangle(v, dx, dy):
    v.corner.x += dx
    v.corner.y += dy


box = Rectangle()
box.width = 50
box.height = 100
box.corner = Point()
box.corner.x = 0
box.corner.y = 0
box2 = copy.deepcopy(box)
print(box2)

move_rectangle(box2,5,5)

print(
    'box1:',
    box.width,
    box.height,
    box.corner.x,
    box.corner.y
)
print(
    'box2:',
    box2.width,
    box2.height,
    box2.corner.x,
    box2.corner.y
)