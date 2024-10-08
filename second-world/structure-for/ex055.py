#leia peso de 5 pessoas, mostre o maior e menor peso
major = minor = 0


for x in range(0,5):
    weight = float(input('Enter with your weight: '))
    if weight > major:
        major = weight
        
    if weight < minor:
        minor = weight

    if x == 0:
        major = minor = weight

print(f'The highest weight is: {major}, and The lowest weight is: {minor}')