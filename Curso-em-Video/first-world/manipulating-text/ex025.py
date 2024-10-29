#Crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome

name = str(input('Enter with your name: ')).lower()

if 'silva' in name:
    print(f'Your name have "silva" ')
else:
    print(f'Your name does not have "silva"')
    