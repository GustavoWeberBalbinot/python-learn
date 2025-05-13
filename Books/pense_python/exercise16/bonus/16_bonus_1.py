'''
Como exercício, escreva uma função chamada print_time, que receba um objeto Time e o exiba na forma hour:minute:second. Dica: a sequência de formatação '%.2d' exibe um número inteiro com, pelo menos, dois dígitos, incluindo um zero à esquerda, se for necessário.
'''

class Time():
    """
    Function to get the time
    Attributes: hour, minute, second
    """

#Yes, I know that minute and second is %60 and hour %12 or 24, but this exercise is to train the class and objects.

time1 = Time()
time1.hour = 15
time1.minute = 23
time1.second = 2
time1.time1 = f'{time1.hour:02d}:{time1.minute:02d}:{time1.second:02d}'

time2 = Time()
time2.hour = 15
time2.minute = 23
time2.second = 3
time2.time2 = f'{time2.hour:02d}:{time2.minute:02d}:{time2.second:02d}'


def analitic_with_if(time1, time2):
    if time1.time1 > time2.time2: #This program, analizing the string to string and the text is the same for they. He see the difference to numbers, and the standard hh:mm:ss
        print(True)
    else:
        print(False)

def analitic_not_if(time1,time2):
    print(f'{time1.time1>time2.time2}')


#analitic_with_if(time1, time2)
analitic_not_if(time1, time2)