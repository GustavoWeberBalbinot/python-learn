#faça uma função que resuma todas as outras em uma só

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

def resumo(valor, aumento, reducao):
    print('-='*30)
    print(f'Resumo do valor {valor}')
    print('-=' * 30)
    print(f'O aumento de {aumento}% do valor {moeda(valor)} = {moeda(aumentar(valor,aumento))}')
    print(f'A diminuição de {reducao}% do valor {moeda(valor)} = {moeda(diminuir(valor, reducao))}')
    print(f'O dobro de {valor} é = {moeda(dobro(valor))}')
    print(f'A metade do {valor} é = {moeda(metade(valor))}')
    print('-=' * 30)
