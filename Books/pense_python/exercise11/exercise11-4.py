"""
Se fez o Exercício 10.7, você já tem uma função chamada has_duplicates, que recebe uma lista como parâmetro e retorna True se houver algum objeto que aparece mais de uma vez na lista.

Use um dicionário para escrever uma versão mais rápida e simples de has_duplicates.
"""

t1 = [1, 2, 3, 4, 5, 1]
t2 = ['apple', 'banana', 'cherry', 'apple']
t3 = ['apple', 'banana', 'cherry']

def has_duplicate(t):
    d = dict()
    for item in t:
        if item not in d:
            d[item] =  1
        else:
            d[item] = d.get(item,0) + 1
    return d

print(has_duplicate(t2))


'''
CHAT GPT:
def has_duplicate(t):
    d = {}
    for item in t:
        if item in d:  # Se o item já existe no dicionário, há um duplicado
            return True
        d[item] = True  # Marca o item como visto              ######Nice logic
    return False  # Se terminar o loop, não há duplicatas
'''