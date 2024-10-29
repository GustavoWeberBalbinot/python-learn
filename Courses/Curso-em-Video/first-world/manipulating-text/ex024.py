#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

city = str(input('Enter with a city name: ')).strip().upper().split()

if city[0] == 'SANTO' or  city[0] == 'SANTA':
    print(f'The city begins with {city[0]}')
else:
    print(f'THe city not begins with SANTO')

