from math import pi, pow
#O volume de uma esfera com raio r é (4/3 * pi * r^3). Qual é o volume de uma esfera com raio 5?

r = 5
v = ((4/3)* pi) * pow(r,3)
#print(v)

#Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?

quantity = 60
cover_price = 24.95
discounted_price = cover_price - (cover_price * 0.4)
transport_cost = 3 + (0.75 * (quantity - 1))
total_cost = (discounted_price * quantity) + transport_cost
#print(f'{total_cost:.2f}')

#Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro), então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa para o café da manhã?

time_exit = 412 #minutes
time_for_km_speed_1 = 8 + 15/60 #minutes
time_for_km_speed_2 = 7 + 12/60 #minutes
time_minute_total= (time_exit + ((time_for_km_speed_1*2) + (time_for_km_speed_2 * 3)))
hour_arrival = int(time_minute_total // 60) #take the int hour
minute_arrival = time_minute_total % 60 #take the float minute
print(f'{hour_arrival}:{minute_arrival:.0f}')
