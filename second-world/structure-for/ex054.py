#pessa idade de 7 pessoas e diga quantas são maiores de idade e quantas são menores de idade:
cont_old = 0
coont_new = 0

for x in range(0,7):
    person = int(input('Enter with your year old: '))
    if person >= 18:
        cont_old += 1
    else:
        coont_new += 1
print(f'The amount of people with a old age, is {cont_old}, and the amount of new age is: {coont_new}')