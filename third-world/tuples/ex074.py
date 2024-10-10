#gerar 5 números aleatórios e colocar na tupla, no final mostrar todos os números, o maior e o menor

from random import randint
greater = lesser = 0

random_numbers_tuple = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))

for x in range(0, 5):
    if x == 0:
        greater = lesser = random_numbers_tuple[x]
    if random_numbers_tuple[x] > greater:
        greater = random_numbers_tuple[x]
    elif random_numbers_tuple[x] < lesser:
        lesser = random_numbers_tuple[x]
    print(f'The {x + 1}º number is: {random_numbers_tuple[x]}')


print(f'The greater number is: {greater}. And the lesser number is: {lesser}')