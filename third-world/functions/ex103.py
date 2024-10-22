#crie uma função ficha(), receba 2 parâmetros, nome e gols.

def ficha(name = '',goals=0):
    if name == '':
        name = 'unknown'
    print(f'The player {name} scored {goals} in the camp')

ficha(str(input('Enter name of the player: ')).strip(), int(input('Enter the goals of the player: ')))
