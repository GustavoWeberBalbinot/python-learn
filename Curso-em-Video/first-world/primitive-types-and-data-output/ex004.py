#Faça um programa que leia algo pelo teclado e mostra na tela o seu tipo primitivo e todas as informações possíveis sobre ele:

something = input('Enter the message: ')

print(f'The message is a word: {something.isalnum()}')
print(f'The message is a number: {something.isalnum()}')
print(f'The message is a letter: {something.isascii()}')
print(f'The message is a lower: {something.islower()}')
print(f'The message is a upper: {something.isupper()}')
print(f'The type of message is: {type(something)}')