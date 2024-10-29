import time

from cadastrar.cadastro import cadastrar_validacao, cadastrar
from listar.listagem import listar

while True:
    print('*-' * 15)
    print('Menu:'.center(30))
    print('*-' * 15)
    condition = '0'
    while condition not in '123':
        condition = str(input('Register person [1]\n'
                              'List people [2]\n'
                              'Exit [3]\n'
                              'Select: '))
    if condition == '1':
        while True:
            name = str(input('Enter a name: ')).strip().capitalize()
            age = str(input('Enter the age: '))
            test = cadastrar_validacao(name, age)
            condition = str(input('Do you want to continue? [Y/N] '))
            if condition in 'Nn':
                break
    if condition == '2':
        listar()
        print('...')
        time.sleep(2)
    if condition == '3':
        print('Thank you, see you later!')
        break
