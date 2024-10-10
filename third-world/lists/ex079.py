#usuário vai digitar váris numeros, registrar eles na lista. Valores já existentes não são adicionados.
#mostrar, todos os valores únicos, em ordem crescente
list_numb = list()

while True:
    numb = int(input('Enter a number: '))
    if numb not in list_numb:
        list_numb.append(numb)
    choice_continue = ' '
    while choice_continue not in 'YN':
        choice_continue = str(input('Do you want continue?[Y/N]: ')).upper()[0]
        break
    if choice_continue in 'N':
        break

list_numb_ordened = sorted(list_numb)
print('The numbers ordened: ', end=' ')
for x in range(0, len(list_numb)):
    print(f'{list_numb_ordened[x]} ', end='')