"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
O primeiro valor é o maior
O segundo valor é o maior
Não exciste valor maior, os dois são iguais.
"""

numb1 = int(input('Enter with a first number: '))
numb2 = int(input('Enter with a second number: '))

if numb1 > numb2:
    print(f'The first {numb1} is greather than second {numb2}')
elif numb2 > numb1:
    print(f'The second {numb2} is greather than  first {numb1}')
else:
    print('This numbers is equal')