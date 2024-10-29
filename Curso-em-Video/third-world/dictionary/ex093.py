#Usuário vai entrar com, nome do jogador de futebul, quantidade de partidas jogadas e gols por partida.
#Mostre todas as informações + total de gols

dict_player = dict()
sum = 0
dict_player['name'] = str(input('Enter a name of soccer player: '))
dict_player['number_matchs'] = int(input('Enter a number of matches playeds: '))
list_matched = list()
for x in range(1, dict_player['number_matchs'] + 1):
    goals = int(input(f'Enter the goals for match {x}: '))
    list_matched.append(goals)
    sum += goals

dict_player['match'] = list_matched
dict_player['sum gols'] = sum

print('-'*30)
for k, v in dict_player.items():
    print(f'The {k} field has the value: {v}')
print('-'*30)
for i, v in enumerate(dict_player['match']):
    print(f'In the {i} the goals is: {v}')
print('-'*30)