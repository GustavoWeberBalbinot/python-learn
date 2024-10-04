#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

numb = int(input('Enter with a number: '))

for x in range(0,11):
    print(f'{numb} x {x} = {numb*x}')
