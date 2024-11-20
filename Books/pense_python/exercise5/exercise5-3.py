"""""
Se você tiver três gravetos, pode ser que consiga arranjá-los em um triângulo ou não. Por exemplo, se um dos gravetos tiver 12 polegadas de comprimento e outros dois tiverem uma polegada de comprimento, não será possível fazer com que os gravetos curtos se encontrem no meio. Há um teste simples para ver se é possível formar um triângulo para quaisquer três comprimentos:

Se algum dos três comprimentos for maior que a soma dos outros dois, então você não pode formar um triângulo. Senão, você pode. (Se a soma de dois comprimentos igualar o terceiro, eles formam um triângulo chamado “degenerado”.)

Escreva uma função chamada is_triangle que receba três números inteiros como argumentos, e que imprima “Yes” ou “No”, dependendo da possibilidade de formar ou não um triângulo de gravetos com os comprimentos dados.

Escreva uma função que peça ao usuário para digitar três comprimentos de gravetos, os converta em números inteiros e use is_triangle para verificar se os gravetos com os comprimentos dados podem formar um triângulo
"""

def is_triangle(a,b,c):
    if a+b >= c and b+c >=a and a+c >= b:
        print('Yes!')
    else:
        print('No! :(')

#user input
a = int(input('Enter with the First side(A): '))
b = int(input('Enter with the Second side(B): '))
c = int(input('Enter with the Third side(C): '))

is_triangle(a,b,c)