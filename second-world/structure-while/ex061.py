#peça um número e seu 10 primeiros termos de sua PA usando while.

numb = int(input('Enter a number: '))
PA = int(input('Enter with a PA for your number: '))
count = 10

print(f'{numb} ', end= '')
while count > 0:
    numb += PA
    print(f'--> {numb}', end='')
    count -= 1


