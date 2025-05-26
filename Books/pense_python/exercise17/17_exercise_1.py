'''
Baixe o código deste capítulo em http://thinkpython2.com/code/Time2.py. Altere os atributos de Time para que um número inteiro único represente os segundos decorridos desde a meia-noite. Então altere os métodos (e a função int_to_time) para funcionar com a nova implementação. Você não deve modificar o código de teste em main. Ao terminar, a saída deve ser a mesma que antes.
'''

class Time:
    """Represents the time of day."""

    def __init__(self, hour=0, minute=0, second=0):
        self.seconds = hour*3600 + minute * 60 + second

    def get_hms(self):
        minutes, second = divmod(self.seconds, 60)
        hour, minute = divmod(minutes, 60)
        return hour, minute, second

    def print_time(self):
        print(str(self))

    def __str__(self):
        hour, minute, second = self.get_hms()
        return '%.2d:%.2d:%.2d' % (hour, minute, second)

    def time_to_int(self):
        seconds = self.seconds
        return seconds

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def __radd__(self, other):
        return self.__add__(other)


def int_to_time(seconds):
    time = Time()
    minutes, time.seconds = divmod(seconds, 60)
    hour, minutes = divmod(minutes, 60)
    return Time(hour, minutes, time.seconds)


def main():
    start = Time(9, 45, 0)
    print("Start time:", start)

    duration = Time(1, 35, 0)
    print("Duration:", duration)

    end = start + duration
    print("End time:", end)

    print("Is end after start?", end.is_after(start))

    print("Incremented by 500 seconds:", start.increment(500))

    total = sum([start, duration, duration])
    print("Sum with radd:", total)


if __name__ == '__main__':
    main()
