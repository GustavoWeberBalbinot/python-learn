#mostre a sequencia de fibonacci de um número inteiro

numb = int(input('Enter a number: '))
first_temporary_numb = 1
second_teporary_numb = 2
third_temporary_numb = 2

print('0 --> 1 --> 1 ', end='')

while third_temporary_numb < numb + 1:
    print(f'--> {third_temporary_numb} ', end='')
    third_temporary_numb = first_temporary_numb + second_teporary_numb
    first_temporary_numb = second_teporary_numb
    second_teporary_numb = third_temporary_numb