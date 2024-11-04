#Escreva uma função chamada right_justify, que receba uma string chamada s como parâmetro e exiba a string com espaços suficientes à frente para que a última letra da string esteja na coluna 70 da tela:

def right_justify(s):
    justify_spaces = 70 - len(s)
    print(' '* justify_spaces, f'{s}')

#right_justify(str(input('Enther a world: ')).strip())

#Defina uma função nova chamada do_four que receba um objeto de função e um valor e chame a função quatro vezes, passando o valor como um parâmetro. Deve haver só duas afirmações no corpo desta função, não quatro.

def do_twice(f, v):
    f(v)
    f(v)

def print_spam(value):
    print(value)
#do_twice(print_spam, 'spam')

def do_four(f,value):
    do_twice(f,value)
    do_twice(f,value)

#do_four(print_spam,'spam')

#Escreva uma função que desenhe uma grade com 4 linhas e 4 colunas:
###
def rown():
    print('- '*4, '+ ',  end='')


def column():
    print( '  '*4, '| ', end='')


def do_draw(function, value_init):
    print(value_init, end='')
    function()
    function()
    print()


def do_three(function, value_init):
    do_draw(function, value_init)
    do_draw(function, value_init)
    do_draw(function, value_init)
    do_draw(function, value_init)


def table(rown, column):
    do_draw(rown,'+ ')
    do_three(column, '| ')
    do_draw(rown,'+ ')
    do_three(column,'| ')
    do_draw(rown,'+ ')

table(rown, column)

""""
CHATGPT Resolution:
def desenhar_grade(linhas, colunas):
    # Parte superior da grade
    parte_superior = "+ " + " - " * 4
    linha_superior = parte_superior * colunas + "+"
    
    # Paredes laterais
    paredes = "| " + "   " * 4
    linha_paredes = paredes * colunas + "|"
    
    # Monta a grade completa
    grade = (linha_superior + "\n" + linha_paredes + "\n") * linhas
    grade += linha_superior  # Adiciona a última linha inferior

    print(grade)

# Chame a função com o número desejado de linhas e colunas
desenhar_grade(2, 2)
"""
