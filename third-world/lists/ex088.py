#programa que gere X jgoos de 6 números entre 1 a 60

from random import randint

random_numb = 0
games_list = list()
temp_list = list()
amount_games = int(input('Enter the desired number of games: '))

print('-=-'*30)
for x in range(0,amount_games):
    for y in range(0,6):
        random_numb = randint(1,60)
        if y == 0:
            temp_list.append(random_numb)
        else:
            while random_numb in temp_list:
                random_numb = randint(1, 60)
            temp_list.append(random_numb)
    games_list.append(temp_list[:])
    temp_list.clear()

games_list_ordened = sorted(games_list)

for x in range(0, amount_games):
    print(f'The game {x + 1}ª is: [ ', end='')
    for y in range(0,6):
        print(f'{games_list_ordened[x][y]} ', end= '')
    print(']')