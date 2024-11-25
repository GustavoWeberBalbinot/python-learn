#A primeira coluna é um número, a; a segunda coluna é a raiz quadrada de a calculada com mysqrt; a terceira coluna é a raiz quadrada calculada por math.sqrt; a quarta coluna é o valor absoluto da diferença entre as duas estimativas.

import math

def mysqrt(a):
    if a > 2:
        x = a - 1
    else:
        x = a
    while True:
        y = (x + a/x) / 2
        if y == x:
            return y
        x = y

user_choice = 0
while user_choice <= 0:    
    user_choice = int(input('Enter with INT number to table of square root: '))
    if user_choice == 0:
        print(f'{user_choice}, cannot be chosen')

actual_numb = 0.0

print(f'{'numb'}\t | \t{'mysqrt(a)'}\t | \t{'math.sqrt(a)'}\t | \t{'diff'}')

while user_choice > actual_numb:
    actual_numb += 1.0
    my_sqrt = mysqrt(actual_numb)
    math_sqrt = math.sqrt(actual_numb)
    diff = math_sqrt - my_sqrt
    print(f'{actual_numb}\t | \t{my_sqrt:.10f}\t | \t{math_sqrt:.10f}\t | \t{diff}')


