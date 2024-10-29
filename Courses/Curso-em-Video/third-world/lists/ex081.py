#leia vários valores bote na lista
#Mostre, qnts numeros foram digitados, lista descrecente, se o valor 5 aparece na lista

numbers_list = list()

while True:
    number_input = int(input('Enter a number: '))
    numbers_list.append(number_input)
    continue_choice = str(input('Do you want continue?[Y/N]: ')).upper()[0]
    if continue_choice in 'N':
        break


print(f'The amount of number entered: {len(numbers_list)}')
print(f'The list in decending order: {sorted(numbers_list, reverse=True)}')
print(f'The number 5 appears: {5 in numbers_list}')
