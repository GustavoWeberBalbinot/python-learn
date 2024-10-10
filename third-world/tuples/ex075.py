#leia 4 valores do teclado, guardar na tupla
#mostrar: qnts vezes apareceu o 9, em que posição o primeiro 3 apareceu, quais foram os números pares

numb_tuple = ( int(input('Enter a first number: ')), int(input('Enter a second number: ')), int(input('Enter a third number: ')), int(input('Enter a fourth number: ')) )

number_nine_amount = 0 #Or use count comand.
even_number = 0
first_three = numb_tuple.index(3)


for x in range(0,4):
    if numb_tuple[x] % 2 == 0:
        even_number += 1
    elif numb_tuple[x] == 9:
        number_nine_amount += 1

print(f'The amount of nine is: {number_nine_amount}')
print(f'The amount of even numbers is: {even_number}')
print(f'The first three appeared in position: {first_three + 1}')