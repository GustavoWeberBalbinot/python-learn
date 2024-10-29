#contar de 10 a 0
from time import sleep

for x in range(10,-1,-1):
    if x >= 1:
        sleep(0.6)
        print(f'Falta {x} segundos!')
    else:
        sleep(2)
        print(f'KABUMM!')

