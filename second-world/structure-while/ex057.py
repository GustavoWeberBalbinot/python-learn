#faça um programa que só aceite o sexo M e F

while True:
    condition = str(input('Enter with your sex [M/F]: ')).upper()[0]
    if condition not in 'MF':
        print('Error, try again')
    if condition in 'MF':
        break
