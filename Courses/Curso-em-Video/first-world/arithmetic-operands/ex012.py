#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

price = float(input('Enter with a price: '))
discount5 = price - (price*0.05)

print(f'With a price {price} you need pay {discount5} with a 5% discount')