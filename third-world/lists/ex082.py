#leia vários números,registre eles em uma lista, crie outras duas listas, uma para numero par e outra para impar

even_list = list()
odd_list = list()
numbers_list = list()

while True:
    numb = int(input('Enter with a number: '))
    numbers_list.append(numb)
    if numb % 2 == 0:
        even_list.append(numb)
    else:
        odd_list.append(numb)
    user_continue = ' '
    while user_continue not in 'YN':
        user_continue = str(input('Do you want continue?[Y/N]: ')).upper()[0]
    if user_continue in 'N':
        break

print(f'The list of numbers: ')
for x in numbers_list:
    print(f'{x} ', end= '')
print()
print(f'The list of even: ')
for x in even_list:
    print(f'{x} ', end= '')
print()
print(f'The list of odd: ')
for x in odd_list:
    print(f'{x} ', end= '')