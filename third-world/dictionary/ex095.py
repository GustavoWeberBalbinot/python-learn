#aprimore o desafio 93, agora deve comportar vários jogadores, incluindo um sistema de vizualização de detalhes do aproveitamento do jogador

players_dict = dict()
player_list = list()
temp_list = list()

while True:
    temp_list.clear()
    players_dict['name'] = str(input('Enter a player: ')).title()
    matches = int(input('Enter a number of matches of this player: '))
    for x in range(0,matches):
        temp_list.append(int(input(f'Enter with goals in the {x} game: ')))
    players_dict['goals'] = temp_list[:]
    players_dict['total goals'] = sum(temp_list)
    player_list.append(players_dict.copy())
    continue_choice = ' '
    while continue_choice not in 'YN':
        continue_choice = str(input('Do you can register new player?: [Y/N]: ')).upper()[0]
    if continue_choice in 'N':
        break

print('cod   ', end='')
for x in players_dict.keys():
    print(f'{x:<15}', end='')
print()
print('-'*30)
for x in range(0,len(player_list)):
    print(f'{x:<5}', end= '')
    print(f'{player_list[x]['name']:<15}', end='')
    print(f'{player_list[x]['goals']}', end='')
    print(f'{player_list[x]['total goals']:>15}')

while True:
    print('-'*30)
    select = int(input('Select a player to view your staticts [999 to stop]: '))
    if select == 999:
        print('See you later!')
        break
    print(f'The player {player_list[select]['name']}, has a score of total gols {player_list[select]['total goals']}')
    for itens, gols in enumerate(player_list[select]['goals']):
        print(f'in matche {itens} has = {gols} goals')