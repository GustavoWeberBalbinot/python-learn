#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numb1 = float(input('Enter with a first number: '))
numb2 = float(input('Enter with a second number: '))
numb3 = float(input('Enter with a third number: '))

if numb1 > numb2 and  numb1 > numb3:
    if numb2 > numb3:
        print(f'The biggest {numb1}, the medium number: {numb2} the smallest number: {numb3}')
    else:
        print(f'The biggest {numb1}, the medium number: {numb3} the smallest number: {numb2}')

elif numb2 > numb1 and numb2 > numb3:
    if numb1 > numb3:
        print(f'The biggest {numb2}, the medium number: {numb1} the smallest number: {numb3}')
    else:
        print(f'The biggest {numb2}, the medium number: {numb3} the smallest number: {numb1}')

elif numb3> numb1 and numb3 > numb2:
    if numb2 > numb1:
        print(f'The biggest {numb3}, the medium number: {numb2} the smallest number: {numb1}')
    else:
        print(f'The biggest {numb3}, the medium number: {numb1} the smallest number: {numb2}')
