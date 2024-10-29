def aumentar(valor, porcentagem, mostrar = False):
    resultado =  valor +(valor * (porcentagem/100))
    if mostrar == True:
        resultado = moeda(resultado)
    return resultado


def diminuir(valor, porcentagem, mostrar = False):
    resultado =  valor -(valor * (porcentagem/100))
    if mostrar == True:
        resultado = moeda(resultado)
    return resultado


def dobro(valor, mostrar = False):
    resultado = valor * 2
    if mostrar == True:
        resultado = moeda(resultado)
    return resultado


def metade(valor, mostrar = False):
    resultado = valor/2
    if mostrar == True:
        resultado = moeda(resultado)
    return resultado

def moeda(texto):
    txt = f'R${texto}'
    return txt
