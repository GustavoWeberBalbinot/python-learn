'''''
O matemático Srinivasa Ramanujan encontrou uma série infinita que pode ser usada para gerar uma aproximação numérica de 1/π:

Fórmula  Aproximação de π pela série de Ramanujan.

Escreva uma função chamada estimate_pi que use esta fórmula para computar e devolver uma estimativa de π(3,14...). Você deve usar o loop while para calcular os termos da adição até que o último termo seja menor que 1e-15 (que é a notação do Python para 10 ** 15). Você pode verificar o resultado comparando-o com math.pi.
'''''

from math import factorial, sqrt
from decimal import Decimal, getcontext


def estimate_pi():
    getcontext().prec = 100
    k = 0
    total = Decimal(0)
    po1 = Decimal(2 * sqrt(2)) / Decimal(9801)
    while True:
        numerator = Decimal(factorial(4 * k)) * (Decimal(1103) + Decimal(26390) * k)
        denominator = (Decimal(factorial(k)) ** 4) * (Decimal(396) ** (4 * k))
        term = numerator / denominator
        total += term
        if term < 1e-15:
            break
        k += 1
    pi_aprox = 1/(po1 * total)
    print(pi_aprox)  
    


estimate_pi()