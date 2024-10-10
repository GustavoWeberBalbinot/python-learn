#Leia, nome, peso de Várias pessoa. Coloque em uma lista
#Mostre quantas pessoas foram cadastradas, pessoas mais pesadas, pessoas mais leves

younger = older = 0
people_list = []
temp = []

while True:
    temp.append(str(input('Enter a name: ')))
    temp.append(int(input('Enter your age: ')))
    if len(people_list) == 0:
        younger = older = temp[1]
    else:
        if temp[1] > older:
            older = temp[1]
        if temp[1] < younger:
            younger = temp[1]
    people_list.append(temp[:])
    condiction = ' '
    while condiction not in 'YN':
        condiction = str(input('Do you want continue? [Y/N]: ')).upper()[0]
    if condiction in 'N':
        break
    temp.clear()

print(f'The amount of peoples: {len(people_list)}')
print(f'The people most older is: {older}')
print(f'The people most younger is: {younger}')

