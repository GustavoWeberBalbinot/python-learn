#Faça funções que recebam valor e porcentagem, e que faça, um aumento, um decremento, dobro, e metade

def increase(value, percentage):
    result = value + (value * (percentage / 100))
    return result


def decrease(value, percentage):
    result = value - (value * (percentage / 100))
    return result


def double(value):
    result = value * 2
    return result


def half(value):
    result = value / 2
    return result

