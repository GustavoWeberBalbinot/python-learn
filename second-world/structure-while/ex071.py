#programa que funcione igual um caixa eletronico, pergunte valor a ser sacado, e quantas notas serão entregues, notas: 50, 20, 10, 1

user_money = int(input('Enter with your money: '))
nota1 = nota2 = nota10 = nota20 = nota50 = 0

while user_money > 0:
    if user_money >= 50:
        user_money -= 50
        nota50 += 1
    elif user_money >= 20:
        user_money -= 20
        nota20 += 1
    elif user_money >= 10:
        user_money -= 10
        nota10 += 1
    elif user_money >= 1:
        user_money -= 1
        nota1 += 1
    
print(f'The amount of 50 bills is: {nota50}')
print(f'The amount of 20 bills  is: {nota20}')
print(f'The amount of 10 bills is: {nota10}')
print(f'The amount of 1 bills is: {nota1}')