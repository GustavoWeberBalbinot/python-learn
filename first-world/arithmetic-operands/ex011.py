#Faça um programa que leia a largura ea altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m^2

height = float(input('Enter with a height[m]: '))
width = float(input('Enter with a width[m]: '))

area = height * width
amount_ink = area / 2
print(f'With a area of {area} you need a amount ink of {amount_ink}')

