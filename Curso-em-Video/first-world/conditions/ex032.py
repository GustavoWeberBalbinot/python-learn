#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

year = int(input('Enter a year: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'This year {year}, is bissextile')
else:
    print(f'This year {year}, not is bissextile')

