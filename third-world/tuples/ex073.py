#crie uma tupla, com os 20 primeiros colocados do futebol
#mostre: 5 primeiros colocados, os 4 ultimos, lista em ordem alfabética, posição na tabela o time atlético mineiro

teams = (('Botafogo', 1), ('Palmeiras', 2), ('Fluminense', 3), ('Grêmio', 4), ('São Paulo', 5), ('Bragantino', 6), ('Flamengo', 7), ('Atlético Mineiro', 8), ('Corinthians', 9), ('Internacional', 10), ('Santos', 11), ('Atlético Goianiense', 12), ('Ceará', 13), ('Bahia', 14), ('Fortaleza', 15), ('Vasco', 16), ('Cruzeiro', 17), ('Coritiba', 18), ('Goiás', 19), ('América Mineiro', 20))
teams_ordened = sorted(teams)

print('The top 5 teams')
for x in range(0,5):
    print(f'The {x + 1}º = {teams[x][0]}')

print('The top last 4 team')
for x in range(19, 15, -1):
    print(f'The {x + 1}º = {teams[x][0]}')

print('The teams ordened: ')
for x in range(0, 20):
    print(f'{teams_ordened[x][0]}')
