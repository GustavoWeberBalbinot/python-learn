#crie uma função voto(), que recebe o ano de nascimento de uma pessoa, e retorna um valor literal, indicando se a pessoa tem voto, negado, opcional, obrigatório.



def voto(user_year):
    from datetime import date
    year_today = date.today().year
    user_year = year_today - user_year
    if user_year < 18:
        txt = 'Denied'
    elif user_year >= 65:
        txt = 'Optional'
    elif user_year >= 18:
        txt = 'Mandatory'
    
    return print(f'Your situation is {txt}')

voto(2022)