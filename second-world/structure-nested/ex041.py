#Faça um programa que leia o ano de nascimento de um atela e mostre sua categoria, de acordo com a idade

from datetime import date

actual_year = date.today().year
birth_year = int(input('Enter with your birth of year: '))
year_old = actual_year - birth_year

if year_old < 9:
    print('Mirim')
elif year_old < 14:
    print('Infantil')
elif year_old < 19:
    print('Junior')
elif year_old == 20:
    print('Sênior')
else:
    print('Master')