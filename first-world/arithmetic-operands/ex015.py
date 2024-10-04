#Escreva um prorama que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o caro custa RS$60 por dia e R$0,15 por km rodado

km_traveled = float(input('Enter with a distance traveled:[km] '))
days_rented = int(input('Enter with the days it rented: '))

price_traveled = km_traveled * 0.15
price_days = days_rented * 60
final_price = price_days + price_traveled

print(f'The price for {days_rented} days rented is: {price_days} and the price for {km_traveled}km traveled is {price_traveled}, the final price is {final_price:.2f}')
