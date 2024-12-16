'''
Escreva uma função chamada middle que receba uma lista e retorne uma nova lista com todos os elementos originais, exceto os primeiros e os últimos elementos. Por exemplo:

>>> t = [1, 2, 3, 4]
>>> middle(t)
[2, 3]
'''
t = [1, 2, 3, 4]

def midle(h):
    last_value = len(h)
    return t[1:last_value - 1]

print(midle(t))