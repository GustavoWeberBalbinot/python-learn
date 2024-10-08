#leia o primeiro termo e sua PA, no final mostre os 10 primeiros termos da sua progressão:

numb = int(input('Enter with a number: '))
PA = int(input('Enter with a PA: '))
for x in range(0, 10):
    if x < 9:
        print(f'{(x*PA)+ numb} -->', end='')
    else:
        print((x*PA)+ numb)
