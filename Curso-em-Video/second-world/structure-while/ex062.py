#peça um número e seu 10 primeiros termos de sua PA usando while. No final pergunte se ele quer mostrar mais termos.


numb = int(input('Enter a number: '))
PA = int(input('Enter with a PA for your number: '))
count = 10

print(f'{numb} ', end= '')
while count > 0:
    numb += PA
    print(f'--> {numb}', end='')
    count -= 1
    if count == 0:
        choice =  str(input('\nDo you want to continue?[Y/N] ')).upper()[0]
        if choice in 'Y':
            count = int(input('How many terms:'))
            continue
        elif choice in 'N':
            break
