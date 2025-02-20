'''
Se há 23 alunos na sua sala, quais são as chances de dois deles fazerem aniversário no mesmo dia? Você pode estimar esta probabilidade gerando amostras aleatórias de 23 dias de aniversário e verificando as correspondências. Dica: você pode gerar aniversários aleatórios com a função randint no módulo random.
'''
from random import randint

days = []
amount = 0 #Variable with the function of counting wheter there(Se há) are equal birth days
test_count = 100 #Amount test to count
simulation_count = 100 #Amount simulation for test

for test in range(test_count):
    for simulation in range(simulation_count):
        for amount_days in range(23):
            days.append(randint(1,365))
        if len(days) != len(set(days)): #Set does not permit duplicate "variables"
            amount += 1
        days.clear()
    
amount_chance = amount / (test_count * simulation_count)

print(f'{amount_chance * 100}%')