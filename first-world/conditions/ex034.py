#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
#Para salários superiores a R$1.250,00 calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.


salary = float(input('Enter with your salary: '))

if salary  > 1250:
    increase = salary * 0.1
else:
    increase = salary * 0.15


print(f'Your salary was {salary}. Your new salary is {salary + increase}')