''''
Escreva uma função chamada nested_sum que receba uma lista de listas de números inteiros e adicione os elementos de todas as listas aninhadas. Por exemplo:
>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
21
'''
t = [[1, 2,[14,15]], [3], [4, 5, 6]]

#No Recursion, this functions is limited
'''''
def nested_sum(t):
    sum_elements = 0
    for sublist in t:
        for elements in sublist:
            sum_elements += elements
    return sum_elements
'''
#With Recursion
def nested_sum(h):
    sum_elements = 0
    if type(h) == int:
        return h
    for list_size in h:
        value = nested_sum(list_size)
        sum_elements += value
    return sum_elements

print(nested_sum(t))
