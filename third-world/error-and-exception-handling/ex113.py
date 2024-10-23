#Crie 2 funções leiaInt() e leiaFloat(), que trataram os seus tipos respectivos, e dirão se é válido ou o tipo de erro.

def readInt(value):
    while True:
        try:
            return int(value)
        except (TypeError, ValueError):
            print('Error, please try again')
            value = str(input('Enter an INTEGER value: '))
        except (KeyboardInterrupt):
            value = 0
            print(f'The user chose not to input, default value is 0')
            return value


def readFloat(value):
    while True:
        try:
            return float(value)
        except (TypeError, ValueError):
            print('Error, please try again: ')
            value = str(input('Enter a REAL value: ').replace(',', '.'))
        except (KeyboardInterrupt):
            value = 0.0
            print(f'The user chose not to input, default value is 0.0')
            return value

valueInt = readInt(str(input('Enter an INTEGER value: ')))
valueFloat = readFloat(str(input('Enter a REAL value: ')).replace(',', '.'))
print(f'The integer value is: {valueInt} and the real value is: {valueFloat}')
