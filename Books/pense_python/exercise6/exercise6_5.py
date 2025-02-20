#O maior divisor comum (MDC, ou GCD em inglês) de a e b é o maior número que divide ambos sem sobrar resto.Um modo de encontrar o MDC de dois números é observar qual é o resto r quando a é dividido por b, verificando que gcd(a, b) = gcd(b, r). Como caso-base, podemos usar gcd(a, 0) = a .Escreva uma função chamada gcd que receba os parâmetros a e b e devolva o maior divisor comum.

def gcd(a, b):
    r = a%b
    if r != 0:
        return gcd(b,r)
    if r == 0:
        return b

print(gcd(101,103))


"""""
CHATGPT

def gcd(a, b):
    if b == 0:  # Caso base: quando b é 0, o MDC é 'a'.
        return a
    return gcd(b, a % b)  # Chamada recursiva com (b, resto).
"""
