#faça um programa que diga se a expressão esta correta com os parenteses abertos e fechados na ordem correta.

expression = str(input('Enter a expression: '))
parentheses = list()

for x in expression:
    if x == '(':
        parentheses.append('(')
    if x == ')':
        if len(parentheses) > 0:
            parentheses.pop()
        else:
            parentheses.append(')')
            break

if len(parentheses) == 0:
    print('This expression is valid')
else:
    print('This expression not is valid')

