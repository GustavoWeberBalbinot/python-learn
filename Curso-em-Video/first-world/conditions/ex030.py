#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR

number = int(input('Enter with a number: '))

if number % 2 == 0:
    print(f'This number {number}, is pair')
else:
    print(f'This number {number}, is  odd')
