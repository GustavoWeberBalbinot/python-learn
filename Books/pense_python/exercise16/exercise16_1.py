'''
Escreva uma função chamada mul_time que receba um objeto Time e um número e retorne um novo objeto Time que contenha o produto do Time original e do número.

Então use mul_time para escrever uma função que receba um objeto Time representando o tempo até o fim de uma corrida e um número que represente a distância, e retorne um objeto Time com o passo médio (tempo por milha).
'''

class Time():
    '''Time, hh:mm:ss
    attributes: hour, minute, second
    '''

time = Time()
time.hour = 2
time.minute = 30
time.second = 25


def time_to_int(time):
    total_seconds = time.hour * 3600 + time.minute * 60 + time.second
    return total_seconds


def int_to_time(value):
    new_time = Time()
    new_time.hour = (value // 3600) % 24
    new_time.minute = (value // 60) % 60
    new_time.second = (value % 60)
    return new_time


def mult_time(time,num):
    new_time = Time()
    seconds_total = int((time_to_int(time)) / num)
    new_time = int_to_time(seconds_total)
    return new_time, num

teste, num = mult_time(time, 15)
print(f'The old time: {time.hour:02d}:{time.minute:02d}:{time.second:02d}')
print(f'The new time: {teste.hour:02d}:{teste.minute:02d}:{teste.second:02d} and the value to divisor is: {num}')
