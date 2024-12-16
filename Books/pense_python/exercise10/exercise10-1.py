''''
Escreva uma função chamada nested_sum que receba uma lista de listas de números inteiros e adicione os elementos de todas as listas aninhadas. Por exemplo:
>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
21
'''
t = [[1, 2], [3], [4, 5, 6]]

def nested_sum(t):
    sum_elements = 0
    for sublist in t:
        for elements in sublist:
            sum_elements += elements
    return sum_elements

print(nested_sum(t))