'''
Como exercício, escreva uma função chamada distance_between_points, que toma dois pontos como argumentos e retorna a distância entre eles.
'''

class point:
    """ 2  Points"""

blank = point()
blank.x = int(input('Enter with a first point: '))
blank.y = int(input('Enter with a second point: '))

def distance_between_points(p):
    distance = p.x - p.y
    if distance < 0:
        distance = distance * -1
    print(f'The distance is:{distance}')

distance_between_points(blank)