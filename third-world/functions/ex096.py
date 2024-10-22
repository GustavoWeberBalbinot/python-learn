#crie uma função, área(), com as dimensões de um terreno, largura e comprimento, e mostre a área do terreno

def area(width, heigt):
    area = width * heigt
    return area

width = int(input('Enter with width of plot:'))
heigth = int(input('Enter with height of plot:'))

print(f'The area of plot with width {width} and {heigth} = {area}')