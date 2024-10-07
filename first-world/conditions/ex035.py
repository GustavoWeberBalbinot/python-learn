#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

side1 = float(input('Enther with a first side: '))
side2 = float(input('Enter with a second side: '))
side3 = float(input('Enter with a third side: '))

if side1 + side2 >= side3 and side2 + side3 >= side1 and side3 + side1 >= side2:
    print(f'These numbers form the triangle')
else:
    print('These numbers dont form the triangle')