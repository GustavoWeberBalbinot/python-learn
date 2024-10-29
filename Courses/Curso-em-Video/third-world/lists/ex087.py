#faça uma matrix 3x3, mostre a soma dos pares, a soma da ultima coluna, o maior valor da segunda linha
#ETornei escalável

matrix = list()
temp = list()
cont = sum_even = sum_last_column = greater_num = 0
size_matrix = 4
range_matrix = size_matrix * size_matrix

for x in range(0,range_matrix):
    temp.append(int(input('Enter a number: ')))
    if temp[cont] % 2 == 0:
        sum_even += temp[cont]
    cont += 1
    if cont == size_matrix:
        matrix.append(temp[:])
        cont = 0
        temp.clear()

for x in range(0,size_matrix):
    for y in range(0,size_matrix):
        if y == size_matrix - 1:
            sum_last_column += matrix[x][y]
        if x == 1:
            if y == 0:
                greater_num = matrix[x][y]
            if  matrix[x][y] > greater_num:
                greater_num = matrix[x][y]
        print(f'[ {matrix[x][y]} ]', end =' ')
    print()

print(f'The sum of even is: {sum_even}')
print(f'The sum of last column: {sum_last_column}')
print(f'The greater number of second row: {greater_num}')