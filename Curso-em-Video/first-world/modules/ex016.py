#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
from math import trunc

real_number = float(input('Enther with a real number: '))

print(f'The {real_number} is float, your whole propotion is {trunc(real_number)}')