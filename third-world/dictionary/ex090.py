#Leia nome, média. Guarde a situação em um dicionário.

dictonary = {'name': '', 'média': '', 'situação': ''}

dictonary['name'] = str(input('Enter student name: '))
dictonary['média'] = float(input('Enter the media: '))

if dictonary['média'] > 7:
    dictonary['situação'] = 'aprovado'
else:
    dictonary['situação'] = 'reprovado'

for k, v  in dictonary.items():
    print(f'{k.ljust(5)}: \t{v}')