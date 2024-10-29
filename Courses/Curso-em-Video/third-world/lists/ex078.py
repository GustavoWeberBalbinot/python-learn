#leia 5 números, guarde na lista
#Mostre, maior e menor e suas posições.

number_list = list()
greater = lester = 0 #Or use the comand, max and min

for x in range(0,5):
    user_number_input = int(input('Enter a number: '))
    number_list.append(user_number_input)


for numb in number_list:
    if greater == 0 and lester == 0:
        greater = lester = numb
    elif numb < lester:
        lester = numb
    elif numb > greater:
        greater = numb

print(f'The greater number is: {greater}, and your position is: {number_list.index(greater) + 1}')
print(f'The lester number is: {lester}, and your position is: {number_list.index(lester) + 1}')