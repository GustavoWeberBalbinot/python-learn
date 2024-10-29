#crie uma tupla, com os números de 0 a 20 por extenso, e o usuário vai pedir por inteiro este número

numbers_tuple = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'tweety')

user_number_choice = int(input('Enter  a number that you want to know: '))

print(f'The number {user_number_choice}, in words is: {numbers_tuple[user_number_choice]}')