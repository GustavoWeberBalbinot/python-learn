'''
Como exercício, escreva uma função chamada move_rectangle que toma um Rectangle e dois números chamados dx e dy. Ela deve alterar a posição do retângulo, adicionando dx à coordenada x de corner e adicionando dy à coordenada y de corner.
'''

class Rectangle():
    """Represents a rectangle:
    attributes: width, height, corner
    """

class Point():
    """Represents a point:
    attributes: x, y
    """


box = Rectangle()
box.width = 50
box.height = 100
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0


def move_rectangle(rec, dx, dy):
    rec.corner.x += dx
    rec.corner.y += dy


move_rectangle(box, 5, 5)
print(
    box.height,
    box.width,
    box.corner.x,
    box.corner.y
)
