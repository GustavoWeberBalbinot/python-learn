'''
Escreva uma função chamada is_sorted que tome uma lista como parâmetro e retorne True se a lista estiver classificada em ordem ascendente, e False se não for o caso. Por exemplo:

>>> is_sorted([1, 2, 2])
True
>>> is_sorted(['b', 'a'])
False

'''

t1 = [1, 2, 2]
t2 = ['b', 'a']

def is_sorted(t):
    for position in range(len(t) - 1):
        if t[position] > t[position + 1]:
            return False
    return True

print(is_sorted(t1))
