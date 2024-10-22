#crie um contador(), que receba, inicio, fim e passo e realize a contagem

def contador(start, end, step):
    if step == 0:
        step = 1
    if start < end:
        print(f'Counting {start} to {end}, with {step} to {step}')
        end += 1
        for x in range(start,end, step):
            print(f'{x} ', end='')
    if start > end:
        if step < 0:
            step *= -1
        print(f'Counting {start} to {end}, with {step} to {step}')
        end -= 1
        for x in range(start,end, - step):
            print(f'{x} ', end='')
    print('END!')

start_numb = int(input('Enter start numb: '))
end_numb = int(input('Enter end numb: '))
step_numb = int(input('Enter steps numb: '))

contador(0, 10, 1)
contador(10, 0, -2)
contador(start_numb, end_numb, step_numb)
