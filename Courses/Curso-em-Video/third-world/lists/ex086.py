#crie uma matrix 3x3
#Eu fiz um programa escalavel

matrix = list()
temp = list()
cont = 0
size_matrix = 3
range_matrix = size_matrix * size_matrix

for x in range(0,range_matrix):
    temp.append(int(input('Enter a number: ')))
    cont += 1
    if cont == size_matrix:
        matrix.append(temp[:])
        cont = 0
        temp.clear()

for x in range(0,size_matrix):
    for y in range(0,size_matrix):
        print(f'[ {matrix[x][y]} ]', end =' ')
    print()
