#leia nome, idade, sexo de 4 pessoas, no final mostre. Média de idade, o homem mais velho, quantas mulheres tem mais de 20 anos

amount_age = 0
sum_age = 0
olddest_man = ''
olddest_man_age = 0
woman_20 = 0

for x in range(0,4):
    name = str(input('Enter with your name: '))
    age = int(input('Enter with your age: '))
    sex = str(input('Enter with your sex [M/F]: ')).upper()[0]
    if olddest_man_age == 0 and sex in 'M':
        olddest_man = name
        olddest_man_age = age

    amount_age += age
    if sex in 'M' and age > olddest_man_age:
        olddest_man = name
        olddest_man_age = age
    if sex in 'F' and age >= 20:
        woman_20 += 1

age_average = amount_age / 4
print(f'The old man is {olddest_man} with a age: {olddest_man_age}')
print(f'The age average is {age_average}')
print(f'The amount of womans with the age above 20 years is: {woman_20}')