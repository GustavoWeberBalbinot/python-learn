#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite

car_speed = float(input('Enter with your car speed: '))

if car_speed > 80:
    price = (car_speed - 80) * 7
    print(f'You have been fined, the price is R${price}')
else:
    print('Nice, you are in maximum speed')
