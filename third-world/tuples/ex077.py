#Crie uma tupla com várias palavras, mostrar para cada palavra, quais são suas vogais.

phrase_tuple = ('amount', 'target', 'rice', 'milk')

from time import sleep

for x in phrase_tuple:
    print(f'For the word: {x} = ', end='')
    for y in x:
        if y in 'aeiou':
            print(f'{y} ' , end='')
    print()
 