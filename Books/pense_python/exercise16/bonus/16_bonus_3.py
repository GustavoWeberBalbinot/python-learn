'''
reescreva increment usando time_to_int e int_to_time.
'''

class Time():
    '''Time 
    '''

time = Time()
time.hour = 2
time.minute = 10
time.second = 30


def time_to_int(time):
    total_seconds = time.hour * 3600 + time.minute * 60 + time.second
    return total_seconds


def int_to_time(value):
    new_time = Time()
    new_time.hour = (value // 3600) % 24
    new_time.minute = (value // 60) % 60
    new_time.second = (value % 60)
    return new_time


def increment(time, value):
    new_value = time_to_int(time)
    total = new_value + value
    return int_to_time(total)

teste = increment(time, 7200)
print(teste.hour)
