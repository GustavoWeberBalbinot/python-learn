#Diga se o triângulo é equilátero, isóceles, escaleno

side1 = float(input('Enter with a first side: '))
side2 = float(input('Enter with a second side: '))
side3 = float(input('Enter with a third side: '))

if side1 + side2 >= side3 and side1 + side3 >= side2 and side2 + side3 >= side1:
    if side1 == side2 and side2 == side3:
        print('This is a equilateral triangle')
    elif side1 == side2 and side1 != side3 or side1 == side3 and side1 != side2:
        print('This is a isosceles triangle')
    else:
        print('This is a scalene triangle')
else:
    print('These numbers dont  form a triangle')
