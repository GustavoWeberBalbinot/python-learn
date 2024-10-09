#leia vários números, mostre no fim, a média, o maior e menor, pergunte se o usuário quer ou não continuar

major = minor = 0
average = 0
sum = 0
count = 0

while True:
    numb = int(input('Enter a number: '))
    if major == 0 and minor == 0:
        major = minor = numb
    elif numb > major:
        major = numb
    elif numb < minor:
        minor = numb
    sum += numb
    count += 1
    choice = str(input('Do you want to continue: [Y/N]')).upper()[0]
    if choice in 'N':
        break

average = sum / count
print(f'The major number is: {major} and minor is: {minor}. The average for the numbers is: {average}')