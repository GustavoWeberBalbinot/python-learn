'''
O módulo datetime fornece objetos time que são semelhantes aos objetos Time deste capítulo, mas ele oferece um grande conjunto de métodos e operadores. Leia a documentação em http://docs.python.org/3/library/datetime.html.

Use o módulo datetime para escrever um programa que receba a data atual e exiba o dia da semana.

Escreva um programa que receba um aniversário como entrada e exiba a idade do usuário e o número de dias, horas, minutos e segundos até o seu próximo aniversário.

Para duas pessoas nascidas em dias diferentes, há um dia em que a idade de uma equivale a duas vezes a da outra. Este é o Dia Duplo delas. Escreva um programa que receba dois aniversários e calcule o Dia Duplo dos aniversariantes.

Para um desafio um pouco maior, escreva a versão mais geral que calcule o dia em que uma pessoa é N vezes mais velha que a outra.
'''

import datetime
import copy
from zoneinfo import ZoneInfo

tz = ZoneInfo("America/Sao_Paulo")
actual_day = datetime.datetime.today()



def actual_week_day(day):
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return week[day.weekday()]



#Birthday exercise



'''birthday = {
    'month': int(input('Put your birth month: ')),
    'day': int(input('Put your birth day: ')),
    'year': int(input('Put your birth year: '))
}'''

birthday = {
    'month': 10,
    'day': 6,
    'year': 2004
}

people_day = datetime.datetime(birthday['year'], birthday['month'], birthday['day'])

def your_age(time):
    days_alive = actual_day - time
    next_birthday = datetime.datetime((actual_day.year),time.month, time.day)
    if actual_day.month - time.month >= 0 and actual_day.day >= time.day:
        next_birthday = datetime.datetime((actual_day.year+1),time.month, time.day)
    next_birthday = next_birthday - actual_day
    print(f'Your live for: {days_alive.days // 365} years. Your next birth days is in: {next_birthday.days} days, {next_birthday.seconds // 3600} hours, {next_birthday.seconds // 60} minutes, {next_birthday.seconds} seconds')
    return 


#your_age(people_day)

#Double day to two people

p1_birthday = datetime.date(2003, 11, 30) #YYYY:MM:DD
p2_birthday = datetime.date(2004, 12, 5) #YYYY:MM:DD


def double_day(p1, p2):
    old = p2 #P2 is expeted to be older
    diff_days = (p1 - p2)
    if diff_days.days == 0:
        print("They do not have a Double Day — they are the same age.")
        return
    if diff_days.days < 0:
        diff_days = abs(diff_days)
        old = p1 #If diff days its negative, p1 to be older
    day = old + diff_days * 2 #Multiplcate to 2 because, to "double day", the Young is X and the Older is 2X
    print(f'The double day is: {day}')


double_day(p1_birthday, p2_birthday)
