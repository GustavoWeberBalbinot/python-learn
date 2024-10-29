#faça um programa que diga se um número é primo

number = int(input('Enter with a number: '))
cont = 0

for x in range(1,number + 1):
    if number % x == 0:
        cont += 1

if cont == 2:
    print('This number is a prime')
else:
    print('This number not is a prime')