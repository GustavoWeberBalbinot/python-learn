'''Escreva uma função chamada choose_from_hist que receba um histograma como definido em “Um dicionário como uma coleção de contadores”, na página 163, e retorne um valor aleatório do histograma, escolhido por probabilidade em proporção à frequência. Por exemplo, para este histograma:

>>> t = ['a', 'a', 'b']
>>> hist = histogram(t)
>>> hist
{'a': 2, 'b': 1}
sua função deve retornar ‘a’ com a probabilidade de 2/3 e ‘b’ com a probabilidade 1/3.'''


t = ['a', 'a', 'b']
t1 = ['a', 'b', 'c', 'd', 'b', 'b', 'a', 'd']


def choose_from_hist(t):
    d = dict()
    count = 0
    for itens in t:
        count += 1
        if itens not in d:
            d[itens] = 0
        value = d[itens]
        d[itens] = value + 1
    for key, values in d.items():
        d[key] = f'{values}/{count}'
    return d

print(choose_from_hist(t1))
