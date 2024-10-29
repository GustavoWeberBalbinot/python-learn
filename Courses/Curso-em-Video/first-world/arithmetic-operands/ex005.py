#Faça um programa que leia um número inteiro e mostre na tela o seu SUCESSOR e seu ANTECESSOR

numb = int(input('Enter with a number: '))

previous_numb = numb - 1
successor_numb = numb + 1

print(f'The number {numb} have a previous: {previous_numb} and successor: {successor_numb}')