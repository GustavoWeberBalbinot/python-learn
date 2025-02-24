'''
Em 1939, Ernest Vincent Wright publicou uma novela de 50.000 palavras, chamada Gadsby, que não contém a letra “e”. Como o “e” é a letra mais comum em inglês, isso não é algo fácil de fazer.

Na verdade, é difícil até construir um único pensamento sem usar o símbolo mais comum do idioma. No início é lento, mas com prudência e horas de treino, vai ficando cada vez mais fácil.

Muito bem, agora eu vou parar.
Escreva uma função chamada has_no_e que retorne True se a palavra dada não tiver a letra “e” nela.

Altere seu programa na seção anterior para imprimir apenas as palavras que não têm “e” e calcule a porcentagem de palavras na lista que não têm “e”.
'''

with open('Books/pense_python/exercise9/moby_words.txt', 'r', encoding='utf-8') as file:
    txt = file.read()

def has_no_e(word):
    if 'e' in word:
        return True
    return False

def percentage_not_e_words(t = str(), see_words = False):
    t = t.split()
    e_count = not_e_count = 0
    for value in t:
        if has_no_e(value):
            if see_words == True:
                print(value)
            e_count += 1
        else:
            not_e_count += 1
    percentage_e = (e_count*100) / len(t)
    percentage_not_e_words = (not_e_count* 100) / len(t)
    print(f"The percentage of words wave the 'E' is:{percentage_e:.2f}")
    print(f"The percentage of words not have the 'E' is:{percentage_not_e_words:.2f}")

percentage_not_e_words(txt)