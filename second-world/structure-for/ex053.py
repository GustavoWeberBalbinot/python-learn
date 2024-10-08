#faça um programa que leia uma frase e diga se ela é ou não um políndromo

phrase = str(input('Enter a phrase: ')).strip().lower().replace(' ', '')
cont = 0
autenticator = 0

for x in range(len(phrase), 0, -1):
    if phrase[x -1] == phrase[cont]:
        cont += 1
        autenticator += 1

if autenticator == len(phrase):
    print('This phrase is a polyndrome')
else:
    print('This phrase dont is a polyndrome')

