'''
Escreva uma função chamada avoids que receba uma palavra e uma série de letras proibidas, e retorne True se a palavra não usar nenhuma das letras proibidas.

Altere o código para que o usuário digite uma série de letras proibidas e o programa imprima o número de palavras que não contêm nenhuma delas. Você pode encontrar uma combinação de cinco letras proibidas que exclua o menor número possível de palavras?
'''

letters_banned = str(input('Enter with the letters banned: '))
with open('Books/pense_python/exercise9/moby_words.txt', 'r', encoding='utf-8') as file:
    txt = file.read()

def avoids(word = str(), letters_banned = str()):
    letters_banned = list(letters_banned)
    word = word.split()
    count_words = 0
    for actual_word in word: #take one word
        count_letters = 0
        for value in letters_banned: #take one letter in the letters banned
            if value not in actual_word:
                count_letters += 1
                if count_letters == len(letters_banned): #"Key" to "break" and analytics all letters
                    count_words += 1
                    print(actual_word)
    return count_words

print(avoids(txt, letters_banned))

#CHAT GPT TIP

'''
def avoids(word: str, letters_banned: str) -> int:
    words = word.split()
    count_words = 0

    for actual_word in words:
        if not any(letter in actual_word for letter in letters_banned):
            count_words += 1
            print(actual_word)

    return count_words

txt = "hello world python code example"
letters_banned = "xw"

print(avoids(txt, letters_banned))
'''
#How to use ANY and ALL
 
# #Difference
'''
any()  |    Pelo menos um elemento for True |   Verificar se uma string contém alguma letra proibida
all()  |	Todos os elementos forem True	|   Verificar se uma string contém todas as letras de uma palavra
'''
#ANY
'''
Retorna True se pelo menos um elemento do iterável for verdadeiro. Caso contrário, retorna False.
Funciona como um "OU lógico" sobre os elementos.

Exemplo:

valores = [False, False, True, False]
print(any(valores))  # True, porque há pelo menos um True

Outro exemplo com strings:

palavra = "hello"
letras_banidas = "xyz"
print(any(letra in palavra for letra in letras_banidas))  # False

Aqui, any() verifica se alguma letra de "xyz" está em "hello".
'''
#ALL
'''
all(iterável)
Retorna True se todos os elementos do iterável forem verdadeiros. Caso contrário, retorna False.
Funciona como um "E lógico" sobre os elementos.

Exemplo:

valores = [True, True, True]
print(all(valores))  # True, pois todos são True

valores = [True, False, True]
print(all(valores))  # False, pois há pelo menos um False

Outro exemplo com strings:

palavra = "hello"
letras_presentes = "helo"
print(all(letra in palavra for letra in letras_presentes))  # True
Aqui, all() verifica se todas as letras de "helo" estão em "hello".
'''

