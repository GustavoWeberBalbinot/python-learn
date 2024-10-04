#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import cos, sin, tan

angle = float(input('Enter with a agle: '))

print(f'The angle {angle} have a sine {sin(angle):.2f} and cosine {cos(angle):.2f} e finally  a tangent {tan(angle):.2f}')