#jokenpô game
from random import randint

machine = ['papel', 'rock', 'scissors']
machine_choise = randint(0,2)
player_choice = int(input('Enter with a play: [1-papel, 2-rock, 3-scissors]: ')) -1

if player_choice == 0 and machine_choise == 1 or player_choice == 1 and machine_choise == 2 or player_choice == 2 and machine_choise == 0:
    print('You win')
elif player_choice == machine_choise:
    print('Draw')
else:
    print(f'You lose, I chose {machine[machine_choise]}')
