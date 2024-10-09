# um programa que mostre várias tábuadas, o programa só para quando o usuário digitar um número negativo

numb = 0
while True:
    numb = int(input('Enter with a numb[Negative number to stop]: '))
    if numb > 0:
        break
    print('-=-'*30)
    for x in range(0,11):
        print(f'{numb} x {x} = {numb * x}')
    print('-=-'*30)

