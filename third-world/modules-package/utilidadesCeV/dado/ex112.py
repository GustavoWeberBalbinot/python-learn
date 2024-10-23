def readMoney(value=''):
    while True:
        if value == '':
            value = 0
        if value.isnumeric():
            value = int(value)
            return value
        else:
            value = str(input('The value is not a number, please try again: '))
