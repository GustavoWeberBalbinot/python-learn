#Crie uma função para verificar se o valor digitado é ou não um número

def leiaint(num = ''):
    if num.isnumeric() is True:
        return int(num)
    else:
        return print(f'This number not is a number')


leiaint(str(input('Enter with a numb: ')).strip())