'''
Mais anagramas!

Escreva um programa que leia uma lista de palavras de um arquivo (veja “Leitura de listas de palavras”, na página 133) e imprima todos os conjuntos de palavras que são anagramas.
        Aqui está um exemplo de como a saída pode parecer:

        ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
        ['retainers', 'ternaries']
        ['generating', 'greatening']
        ['resmelts', 'smelters', 'termless']
        Dica: você pode querer construir um dicionário que mapeie uma coleção de letras a uma lista de palavras que podem ser soletradas com essas letras. A pergunta é: como representar a coleção de letras de forma que possa ser usada como uma chave?

Altere o programa anterior para que exiba a lista mais longa de anagramas primeiro, seguido pela segunda mais longa, e assim por diante.

No Scrabble, um “bingo” é quando você joga todas as sete peças na sua estante, junto com uma peça no tabuleiro, para formar uma palavra de oito letras. Que coleção de oito letras forma o maior número possível de bingos? Dica: há sete.
'''



with open('Books/pense_python/exercise12/file.txt', 'r') as file:
    conteudo = file.read()
    itens = conteudo.lower().split(';')


def detect_anagram_words(list_words = list()):
    awords = dict()
    for item in list_words:
        word = str(sorted(item)) #This part organize the word in aphabetical sequence in list, the same sequence = anagram
        if word not in awords:
                awords[word] = [item] #if the word not in dict, add this sequence word and your item
        else:
                awords[word].append(item) #if the word in dict, append the item in the X sequence
    awords = list_itens_dict(awords.values()) #Geting the values of amount the anagrams equals and "joining"
    for x in sorted(awords, reverse=True): #This part get the descending values and print in the screen
        for sequence in awords[x]:
            print(f'{x} {sequence} ')
        print('')
    return awords



def list_itens_dict(d):
    inverse = dict()
    for key in d:
        value = len(key) #Get the amount itens have in the key
        if value not in inverse:
            inverse[value] = [key] #if this item not in dict, add the item in value with your item
        else:
            inverse[value].append(key) #this part add the key in x value
    return inverse


detect_anagram_words(itens)


'''
CHATGPT
################JOIN IS VERY OVERPOWER:

with open('Books/pense_python/exercise11/file.txt', 'r') as file:
    conteudo = file.read()
    itens = conteudo.lower().split(';')


def detect_anagram_words(list_words):
    anagram_dict = {}

    # Criando o dicionário de anagramas
    for word in list_words:
        key = "".join(sorted(word))  # Ordena as letras da palavra para formar a chave
        anagram_dict.setdefault(key, []).append(word)

    # Filtrando apenas os grupos que possuem mais de um anagrama
    anagram_groups = [words for words in anagram_dict.values() if len(words) > 1]

    # Ordenando os grupos de anagramas do maior para o menor
    anagram_groups.sort(key=len, reverse=True)

    # Exibindo os resultados
    for group in anagram_groups:
        print(f"{len(group)} {group}\n")

    return anagram_groups


detect_anagram_words(itens)
'''