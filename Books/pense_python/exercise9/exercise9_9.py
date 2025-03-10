'''
“Há pouco tempo recebi uma visita da minha mãe e percebemos que os dois dígitos que compõem a minha idade, quando invertidos, representavam a idade dela. Por exemplo, se ela tem 73 anos, eu tenho 37 anos. Ficamos imaginando com que frequência isto aconteceu nos anos anteriores, mas acabamos mudando de assunto e não chegamos a uma resposta.

“Quando cheguei em casa, cheguei à conclusão de que os dígitos das nossas idades tinham sido reversíveis seis vezes até então. Também percebi que, se tivéssemos sorte, isso aconteceria novamente dali a alguns anos, e se fôssemos muito sortudos, aconteceria mais uma vez depois disso. Em outras palavras, aconteceria 8 vezes no total. Então a pergunta é: quantos anos tenho agora?”

Escreva um programa em Python que busque soluções para esse problema. Dica: pode ser uma boa ideia usar o método de string zfill.'''


#Statment is wrong ZZZZZZZZZZZZZZZ

mother_age = 73
child_age = 37
age_diff = mother_age - child_age
mother_age_now = age_diff



def invert(numb):
    numb = str(numb)
    numb = numb[::-1]
    numb = int(numb)
    return numb


for child_age_now in range(0,100):
    if child_age_now == invert(mother_age_now):
        print(f'child age x:{child_age_now} and mother age y:{mother_age_now}')
    mother_age_now +=  1
    
