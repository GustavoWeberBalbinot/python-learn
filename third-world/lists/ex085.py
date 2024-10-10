#User input 7 numbers, organize in even and odd list ordened

even_list = list()
odd_list = list()

for x in range(0, 7):
    numb_input = int(input('Enter a number: '))
    if numb_input % 2 == 0:
        even_list.append(numb_input)
    else:
        odd_list.append(numb_input)

even_list_ordened = sorted(even_list)
odd_list_ordened = sorted(odd_list)

print(f'The list of even numbers ordened is: {even_list_ordened}')
print(f'The list of odd numbers ordened is: {odd_list_ordened}')