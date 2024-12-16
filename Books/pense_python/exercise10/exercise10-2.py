'''
Escreva uma função chamada cumsum que receba uma lista de números e retorne a soma cumulativa; isto é, uma nova lista onde o i-ésimo elemento é a soma dos primeiros i+1 elementos da lista original. Por exemplo:

>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]
'''

t = [1, 2, 3]

def cumsum(h):
    new_numb_list = []
    numb_sum = 0
    for x in h:
        numb_sum += x
        new_numb_list.append(numb_sum)
    return new_numb_list


cumsum(t)
