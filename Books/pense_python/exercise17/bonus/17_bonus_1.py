'''
Como exercício, reescreva time_to_int (de “Prototipação versus planejamento”, na página 234) como um método. Você pode ficar tentado a reescrever int_to_time como um método também, mas isso não faz muito sentido porque não haveria nenhum objeto sobre o qual invocá-lo.
'''


class Time:
    '''Work with time
    attributes: hour, minute, second
    '''
    def __init__(self, hour=0, minute=0, seconds=0):
        self.hour = hour
        self.minute = minute
        self.seconds = seconds


    def time_to_int(self):
        seconds_int = self.hour * 3600 + self.minute * 60 + self.second
        return seconds_int

test = Time()
test.hour = 1
test.minute = 60
test.second = 60
print(test.time_to_int())

'''
1-Como exercício, escreva um método str da classe Point. Crie um objeto Point e exiba-o.

2-Como exercício, escreva um método add para a classe Point.

3-Como exercício, escreva um método add para Points que funcione com um objeto Point ou com uma tupla:
    Se o segundo operando for um Point, o método deve retornar um novo Point cuja coordenada x é a soma das coordenadas x dos operandos, e o mesmo se aplica às coordenadas de y.
    Se o segundo operando for uma tupla, o método deve adicionar o primeiro elemento da tupla à coordenada de x e o segundo elemento à coordenada de y, retornando um novo Point com o resultado.
'''

class Point():
    '''This class, receive the 1 coordinate point
    attributes: x, y
    '''
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def __str__(self):
        return (f'Point X: {self.x} Point Y: {self.y}')
    

    def __add__(self,other):
        if isinstance(other, Point): #I need to pass the object
            return self.add_points(other)
        else:
            return self.add_tuple_points(other)
        
    
    def add_points(self,other):
        value_x = self.x + other.x
        value_y = self.y + other.y
        return Point(value_x, value_y)
    

    def add_tuple_points(self, other=tuple()):
        value_x = other[0] + self.x
        value_y = other[1] + self.y
        return Point(value_x, value_y)
    

    def __radd__(self, other): #Invert SELF and OTHER in position.
        return self.__add__(other)



p = Point(5, 10)
pp = Point(15, 25)
print(p + (15,25))
print((15,25) + p)