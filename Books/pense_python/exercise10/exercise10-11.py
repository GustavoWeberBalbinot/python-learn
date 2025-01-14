'''
Duas palavras são um “par inverso” se uma for o contrário da outra. Escreva um programa que encontre todos os pares inversos na lista de palavras.
'''

palavras = [
    "roma", "amor", "pato", "livro", "asac", "casa", "zebra", "rever", 
    "zul", "sol", "python", "nohtyp", "gato", "otap", "arara", "random", 
    "radar", "carro", "orrac", "otag", "estrela", "ovo", "luz", "galaxy"
]


def inverse_pair(list_words=list()):
    words_pair = list()
    for item in list_words:
        break_Value = 0 #This value is used to break repeated itens
        for sublist in words_pair: #Checking the words in the list: words_pair. The FOR is necessary to acess sublist[[item1, item2]]
            if item in sublist:
                break_Value = 1
        if break_Value != 1:
            inverse_item = item[::-1]
            if inverse_item in list_words:
                words_pair.append([item, inverse_item])
    return words_pair


print(inverse_pair(palavras))

'''
CHAT GPT ---- OMG #SET# ITS VERY OVER POWER

def inverse_pair(list_words):
    words_pair = []
    checked_words = set()  # Usar um conjunto para rastrear palavras já processadas

    for word in list_words:
        if word in checked_words:  # Pule palavras já verificadas
            continue
        inverse_word = word[::-1]
        if inverse_word in list_words and inverse_word != word:
            words_pair.append([word, inverse_word])
            checked_words.add(word)
            checked_words.add(inverse_word)  # Evitar pares duplicados

    return words_pair
'''