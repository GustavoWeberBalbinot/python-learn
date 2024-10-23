#Melhore o ex107 e adicione um "texto de cifra" para os valores

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


def currency(text):
    txt = f'R${text}'
    return txt
