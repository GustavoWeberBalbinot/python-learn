'''
Memorize a função de Ackermann do Exercício 6.2 e veja se a memorização permite avaliar a função com argumentos maiores. Dica: não.
'''
#Chatgpt help me

know = {}

def ackermann(m, n):
    if (m,n) in know:
        return know[(m,n)]
    if m == 0:
        res = n + 1
    if m > 0 and n == 0:
        res = ackermann(m -1, 1)
    if m > 0 and n > 0:
        res = ackermann(m - 1, ackermann(m, n -1))
    know[(m,n)] = res
    return res

print(ackermann(3,4))
