#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salary = float(input('Enter with your salary R$: '))
new_salary = salary + (salary*0.15)

print(f'Your new salary is {new_salary} with a 15% increase')
