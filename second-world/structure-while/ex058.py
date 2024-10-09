#Jogador precissa acertar o número da máquina, só acaba quando ele acertar
from random import randint
number = randint(0,10)
while True:
    player = int(input('Enter with a number[0-10]: '))
    if player == number:
        print('Your answer is correct, nice')
        break
    else:
        print('Error, try again')
    
