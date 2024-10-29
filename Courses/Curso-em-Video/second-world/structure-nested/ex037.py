#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário:
#2 para octal:
#3 para hexadecimal:

num = int(input('Enter with a number: '))
print('Conversion this number to:')
print('1 - Binary')
print('2 - Octal')
print('3 - Hexadecimal')
choice = int(input('Enter with a choice: '))

if choice == 1:
    print(f'This number {num} converted to binary is: {bin(num)}')
elif choice == 2:
    print(f'This number {num} converted to octal is: {oct(num)}')
elif choice == 3:
    print(f'This number {num} converted to hexadecimal is: {hex(num)}')