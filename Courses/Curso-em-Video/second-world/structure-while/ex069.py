#leia, idade, sexo de várias pessoas, pergunte se o usuário quer continuar. Cadastre, maiores de 18, quantos homens, quantas mulheres acima de 20

legalAge_amount = mans = womans_20 = 0


while True:
    age = int(input('Enter your age: '))
    gender = str(input('Enter your gender[M/F]: ')).upper()[0]
    if age > 18:
        legalAge_amount += 1
    if gender in 'M':
        mans += 1
    elif gender in 'F' and age > 20:
        womans_20 += 1
    choice_continue = str(input('Do you need continue? [Y/N]: ')).upper()[0]
    if choice_continue in 'N':
        break

print(f'The legal Age amount is: {legalAge_amount}')
print(f'The amount of mans is {mans}')
print(f'The amount of womans aged over 20: {womans_20}')