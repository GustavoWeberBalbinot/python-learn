#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint

number_computer = randint(0,5)

print('Lets play a game, try to guess a number from 0 to 5')
number_choicer = int(input('Enther with a number between 0 to 5: '))

if number_choicer == number_computer:
    print(f'Yes, you got it right, the number was: {number_computer}')
else:
    print(f'No, you wrong the number, the number was: {number_computer} ')

