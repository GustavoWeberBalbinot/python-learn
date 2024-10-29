#um programa que peça 2 números, e o usuário deve escolher uma operação.

while True:
    numb1 = float(input('Enter a first number: '))
    numb2 = float(input('Enter a second number: '))
    print('[1] sum')
    print('[2] multiply')
    print('[3] major')
    print('[4] new numbers')
    print('[5] leave the program')
    user_choice = int(input('Enter with your choice: '))
    if user_choice == 1:
        print(f'{numb1} + {numb2} = {numb1 + numb2}')
    elif user_choice == 2:
        print(f'{numb1} x {numb2} = {numb1 * numb2}')
    elif user_choice == 3:
        if numb1 > numb2:
            print(f'The major number is: {numb1}')
        else:
            print(f'The major number is: {numb2}')
    elif user_choice == 4:
        continue
    elif user_choice == 5:
        print('Thanks, See you later')
        break
    else:
        print('Error, this choice not found')
