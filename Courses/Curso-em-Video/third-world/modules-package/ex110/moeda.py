#faça uma função que resuma todas as outras em uma só

def increase(value, percentage, show=False):
    result = value + (value * (percentage / 100))
    if show:
        result = currency(result)
    return result


def decrease(value, percentage, show=False):
    result = value - (value * (percentage / 100))
    if show:
        result = currency(result)
    return result


def double(value, show=False):
    result = value * 2
    if show:
        result = currency(result)
    return result


def half(value, show=False):
    result = value / 2
    if show:
        result = currency(result)
    return result


def currency(text):
    txt = f'R${text}'
    return txt


def summary(value, increase_pct, decrease_pct):
    print('-=' * 30)
    print(f'Summary of the value {value}')
    print('-=' * 30)
    print(f'The increase of {increase_pct}% of the value {currency(value)} = {currency(increase(value, increase_pct))}')
    print(f'The decrease of {decrease_pct}% of the value {currency(value)} = {currency(decrease(value, decrease_pct))}')
    print(f'The double of {value} is = {currency(double(value))}')
    print(f'The half of {value} is = {currency(half(value))}')
    print('-=' * 30)
