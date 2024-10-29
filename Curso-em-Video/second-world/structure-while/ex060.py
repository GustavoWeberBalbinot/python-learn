#o programa mostre o fatorial de um número

numb = int(input('Enter a number: '))
answer = 0
factorial = numb - 1

print(f'{numb}! = {numb}', end= '')

while factorial != 0:
    numb = factorial * numb
    print(f' x {factorial} ', end='')
    factorial -= 1


answer = numb
print(f'= {answer}')