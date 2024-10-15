#Leia, nome, sexo idade de várias pessoas. Guarde em um dicionário, e depois em uma lista.
#Mostre: Quantidade de pessoas cadastradas, Média da idade, Lista com as mulheres, Lista com pessoas acima da média

people_dict = dict()
people_list = list()

while True:
    people_dict['name'] = str(input('Enter a name: ')).title()
    people_dict['gender'] = str(input('Enter a gender:[M/F] ')).upper()[0]
    people_dict['age'] = int(input('Enter a age: '))
    people_list.append(people_dict.copy())
    continue_choice = str(input('Do you want continue?[Y/N]: ')).upper()[0]
    if continue_choice in 'N':
        break

print('-'*30)
quantity_people = len(people_list)
print(f'The quantity of people: {quantity_people}')
average = 0
for x in range(0,len(people_list)):
    average += (people_list[x]['age'])

average = average/quantity_people

print(f'The average of age: {average:.2f}')
print(f'The list of womans is: ', end='')
for x in range(0, len(people_list)):
    if people_list[x]['gender'] in 'F':
        print(f' {people_list[x]['name']}', end= '')
print(f'\n List with the peoples above the average age {average:.2f}: ')
for x in range(0,len(people_list)):
    if people_list[x]['age'] >= average:
        print(f'The people: {people_list[x]['name']}, years old {people_list[x]['age']}')
print('-'*30)