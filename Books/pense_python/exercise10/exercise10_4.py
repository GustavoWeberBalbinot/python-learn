'''
Escreva uma função chamada chop que tome uma lista alterando-a para remover o primeiro e o último elementos, e retorne None. Por exemplo:

>>> t = [1, 2, 3, 4]
>>> chop(t)
>>> t
[2, 3]

'''
t = [1, 2, 3, 4]

def chop(t):
    del t[0] 
    del t[-1]
    return None

print(chop(t))
print(t)
