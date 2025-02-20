# Em sistemas UNIX, a época é primeiro de janeiro de 1970.
#Escreva um script que leia a hora atual e a converta em um tempo em horas, minutos e segundos, mais o número de dias desde a época.
import time
time =time.time()
seconds = time % 60
minutes = time // 60 % 60
hours = (time//3600) % 24
br_hours = hours - 3
days = (time//86400)
print(f'UTC : Days: {days:.2f}, the time is: {int(hours)}:{int(minutes)}:{int(seconds)}')
print(f'BR : Days: {days:.2f}, the time is: {int(br_hours)}:{int(minutes)}:{int(seconds)}')