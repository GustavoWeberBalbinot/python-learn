'''
Como exercício, escreva um método __lt__ para objetos Time. Você pode usar uma comparação de tuplas, mas também pode usar a comparação de números inteiros.
'''

class Time():
    '''Define time, dd:mm:ss
    attributes: hour, minute, second
    '''
    
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def get_hms(self):#"Format" the time
        seconds = self.hour * 3600 + self.minute * 60 + self.second
        minute, seconds = divmod(seconds, 60)
        hour, minute = divmod(minute, 60)
        return hour, minute, seconds

    def __lt__(self, other):
        t1 = self.get_hms()
        t2 = other.get_hms()
        return t1 < t2
    

teee1 = Time(2,30,45)
teee2 = Time(2,33,45)
print(teee1 < teee2)