#Um programa que leai vários números int,  o programa para com o digito 999, no final mostre quantos números foram digitados e sua soma.

sum = 0
count = 0

while True:
    numb = int(input('Enter a number, [999 to stop]: '))
    if numb == 999:
        break
    count += 1
    sum += numb

print(f'The amount of numbs: {count} and the sum of all numbers is {sum}')
    