#Um número a é uma potência de b se for divisível por b e a/b for uma potência de b. Escreva uma função chamada is_power que receba os parâmetros a e b e retorne True se a for uma potência de b. Dica: pense no caso-base.
import math



def is_power(a, b, c=1):
    if a % b == 0:
        if a/b == math.pow(b, c):
            return True
        else:
            return is_power(a, b, c + 1)
    else:
        return False

print(is_power(27,3))


"""""
Eu adicionei um contador, não era preciso/usuário pode fazer cagada com ele. Eu fiz com que B fosse multiplicado por C(que vai aumentando de 1 em 1), até chegar no valor de A. (Problema do meu, C é um problema que o usuário pode mexer, math.pow pode gerar problemas, e a complexidade do código)
Chatgpt, fez com que o A fosse dividido por b, até chegar em 1 para True.

Chatgpt resolution:
def is_power(a, b):
    if a == 1:
        return True
    if a % b != 0:
        return False
    return is_power(a // b, b)

# Testando
print(is_power(27, 3))  # True
print(is_power(8, 2))   # True
print(is_power(10, 2))  # False
"""
