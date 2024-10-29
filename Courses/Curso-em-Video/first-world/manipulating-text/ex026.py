#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "a"
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez.


phrase = str(input('Enter with a phrase: ')).lower().strip().replace(' ', '')
a_count = phrase.count('a')
a_first = phrase.find('a') + 1
a_last = phrase.rfind('a') + 1


print(f'The ammountt of "a" is: {a_count}')
print(f'The letter "a"  appears the first time in the position: {a_first}')
print(f'The last "a" appears in the position: {a_last}')