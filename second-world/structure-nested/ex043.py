#faça o calculo de IMC

weight = float(input('Enter with your weight: '))
height = float(input('Enter with your height: '))
imc = weight/(height*height)

if imc < 18.5:
    print('Underweight')
elif imc >= 18.5 and imc < 25:
    print('Ideal weight')
elif imc >= 25 and imc < 30:
    print('Overweight')
elif imc >= 30 and imc < 40:
    print('Obesity')
else:
    print('Morbid obesity')
