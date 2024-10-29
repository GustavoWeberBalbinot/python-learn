#função, fatorial(), que receba o número, e o 'show' um valor lógico (opcional) indicando se deve mostrar ou não na tela o processo do calculo

def fatorial(numb=0, show=False):
    if numb == 0:
        numb = 1
    sum_numbs = 1
    print(f'{numb}! =', end='')
    for x in range(numb, 0, -1):
        if show == True:
            print(f' {x} x' if x > 1 else f' {x} =', end='')
        sum_numbs = x * sum_numbs
    print(f' {sum_numbs}')

fatorial(5, show=True)
