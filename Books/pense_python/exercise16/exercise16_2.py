'''
O módulo datetime fornece objetos time que são semelhantes aos objetos Time deste capítulo, mas ele oferece um grande conjunto de métodos e operadores. Leia a documentação em http://docs.python.org/3/library/datetime.html.

Use o módulo datetime para escrever um programa que receba a data atual e exiba o dia da semana.

Escreva um programa que receba um aniversário como entrada e exiba a idade do usuário e o número de dias, horas, minutos e segundos até o seu próximo aniversário.

Para duas pessoas nascidas em dias diferentes, há um dia em que a idade de uma equivale a duas vezes a da outra. Este é o Dia Duplo delas. Escreva um programa que receba dois aniversários e calcule o Dia Duplo dos aniversariantes.

Para um desafio um pouco maior, escreva a versão mais geral que calcule o dia em que uma pessoa é N vezes mais velha que a outra.
'''

import datetime
from zoneinfo import ZoneInfo

actual_day = datetime.date.today()



def actual_week_day(day):
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return week[day.weekday()]



#Birthday exercise



'''birthday = {
    'month': int(input('Put your birth month: ')),
    'day': int(input('Put your birth day: ')),
    'year': int(input('Put your birth year: '))
}
people_day = datetime.date(birthday['year'], birthday['month'], birthday['day'])'''
today_actual = datetime.date.today()
teste = datetime.timedelta(seconds=11235813)
print(teste.seconds)