#A função integrada eval toma uma string e a avalia, usando o interpretador do Python. Por exemplo:

#Escreva uma função chamada eval_loop que iterativamente peça uma entrada ao usuário, a avalie usando eval e exiba o resultado.
#Ela deve continuar até que o usuário digite done; então deverá exibir o valor da última expressão avaliada.


def eval_loop(expression):
    while True:
        print(eval(expression))
        expression = str(input('Enter with a expression, [done] to stop: ')).strip().lower()
        if expression == 'done':
            break

user_expression = str(input('Enter with a expression: '))  
eval_loop(user_expression)