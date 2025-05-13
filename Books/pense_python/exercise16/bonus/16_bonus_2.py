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

'''increment(time, 10000)
print(f'{time.hour:02d}:{time.minute:02d}:{time.second:02d}')'''


'''
Como exercício, escreva uma versão “pura” de increment que cria e retorna um objeto Time em vez de alterar o parâmetro.
'''

def increment_pure(time, seconds):
    pure_time = Time()
    total_seconds = time.second + seconds
    pure_time.second =  total_seconds % 60
    total_minutes = total_seconds // 60
    total_minutes += time.minute
    pure_time.minute = total_minutes % 60
    pure_time.hour = (time.hour + total_minutes // 60) % 24
    return f'The new time is:{pure_time.hour:02d}:{pure_time.minute:02d}:{pure_time.second:02d}'

print(f'The old time is:{time.hour:02d}:{time.minute:02d}:{time.second:02d}')
print(increment_pure(time, 10000))