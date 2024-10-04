#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
from math import pow, sqrt


cateto_oposto = float(input('Enter with a cateto oposto: '))
cateto_adjacente = float(input('Enther with a cateto adjacente: '))

hipotenusa = pow(cateto_adjacente, 2) + pow(cateto_oposto, 2)

print(f'The hipotenusa is {sqrt(hipotenusa)}')