#jogo de par ou impar com a máquina e jogador, só para quando o jogador perde, mostre o total de vitórias do jogador

from random import randint

victory = 0

while True:
    machine = randint(0, 10)
    player = int(input('Enter with a number [0 to 10]: '))
    if player == machine:
        print('You win, lets play again')
        victory += 1
    if player != machine:
        print(f'You lose I chose {machine}')
        break

print(f'The amount of victory the player is: {victory}')