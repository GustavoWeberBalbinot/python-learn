'''
Como exercício, reescreva avoids usando conjuntos.
'''

def avoids(word, forbidden):
    return not any(w in set(forbidden) for w in word)


print(avoids('horse', 'tttt'))