#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Ex: Digite 1834
#unidade:4
#dezena:3
#centena:8
#milhar:1
num = int(input('Enter with a number between 0 to 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'The number {num} have unit {u} have ten {d} have hundred {c} have thousand {m}')