#Desenvolva um programa que pergunte a distância de uma viagem em KM.
#Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200KM e R$0,45 para viagens mais longas

distance = float(input('Enter with a distance traveled: '))

if distance > 200:
    price = distance * 0.45
    print(f'With distance equal {distance} the price is: R${price} to R$0.45 for distance')
else:
    price = distance * 0.5
    print(f'With distance equal {distance} the price is: R${price} to R$0.50 for distance')

