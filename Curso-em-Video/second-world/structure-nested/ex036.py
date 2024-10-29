#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode excede 30% do salário ou então o empréstimo será negado

house_value = float(input('Enter with a house value: '))
person_salary = float(input('Enter with your salary value: '))
years = float(input('Enter with years for parcel: '))

years_parcel = years * 12
month_parcel = house_value / years_parcel 


if month_parcel > (person_salary * 0.3):
    print(f'Your loan was denied')
else:
    print(f'Your loan was accept, the moth parcel is: {month_parcel:.2f}')
