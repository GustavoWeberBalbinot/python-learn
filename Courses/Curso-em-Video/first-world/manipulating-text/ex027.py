#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente.
#Ex: Ana Maria de Souza
#Primeiro= Ana
#Último = Souza

name = str(input('Enter with your name: ')).title().split()

print(f'Welcome, your fist name is: {name[0]}, and the last name is {name[-1]}')
