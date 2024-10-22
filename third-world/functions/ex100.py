#crie uma lista com números, e duas funções, sorteia() e somaPar(). sortei 5 números e coloques dentro da lista. segunda função vai somar apenas os pares da função anterior
from random import randint

num_list = list()

def sorteia():
    for x in range(0,5):
        num_list.append((randint(0,10)))
    return num_list

def somaPar(num):
    sum_even_numbs = 0
    for x in range(0,len(num)):
        if num[x] % 2 == 0:
            sum_even_numbs += num[x]
    return sum_even_numbs

print(sorteia())
print(somaPar(num_list))