#ler 6 numeros inteiros, mostrar a soma de apenas aqueles que forem par
sum_numbers = 0

for x in range(1,7):
    numb = int(input(f'Enter with a number {x}: '))
    if numb % 2 == 0:
        sum_numbers += numb

print(sum_numbers)