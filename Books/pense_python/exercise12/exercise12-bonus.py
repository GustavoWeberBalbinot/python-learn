'''
Como exercício, escreva uma função chamada sumall que receba qualquer número de argumentos e retorne a soma deles.
'''

def sumall(*args):
    sum = 0 + args
    for x in (args):
        sum += x
    return sum

print(sumall(1,2,3,4,5,6))
