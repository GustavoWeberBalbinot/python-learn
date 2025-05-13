'''
Como exercício, escreva uma versão correta de increment que não contenha loops.
'''

class Time():
    '''Time class
    '''

time = Time()
time.hour = 15
time.minute = 16
time.second = 23



def increment(time, seconds):
    total_seconds = time.second + seconds
    time.second =  total_seconds % 60
    total_minutes = total_seconds // 60
    total_minutes += time.minute
    time.minute = total_minutes % 60
    time.hour = (time.hour + total_minutes // 60) % 24
    return

increment(time, 10000)
print(f'{time.hour:02d}:{time.minute:02d}:{time.second:02d}')
