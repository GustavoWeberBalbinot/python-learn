'''
Duas palavras “interligam-se” quando, ao tomarmos letras alternadas de cada uma, formamos uma palavra nova. Por exemplo, “shoe” e “cold” interligam-se para formar “schooled”.

Escreva um programa que encontre todos os pares de palavras que se interligam. Dica: não enumere todos os pares!

Você pode encontrar palavras que sejam interligadas de três em três; isto é, cada terceira letra forma uma palavra, começando da primeira, segunda ou terceira?
'''

from spellchecker import SpellChecker

list_words = [
    "livro" , "estrada", "leão", "borboleta", "flor", 
    "computador", "livro", "carro", "praia", "sol", 
    "estrela", "floresta", "bicho", "gato", "arvore"
]


def interconnect_words(words_to_test = list()):
    new_words_list = list()
    third_value = last_word = False
    if len(words_to_test) % 2 != 0: #If to verify the amount of words in the list its odd
        last_word = True
    for x in range(1, len(words_to_test),2):
        new_word = ''
        if x == len(words_to_test) - 1 and last_word:
            max_value = max(len(words_to_test[x-1]), len(words_to_test[x]), len(words_to_test[x+1]))  
            last_word = True  
        else:
            max_value = max(len(words_to_test[x-1]), len(words_to_test[x]))
        for y in range(max_value):
            if y < len(words_to_test[x - 1]):
                new_word = new_word + words_to_test[x-1][y]
            if y < len(words_to_test[x]):
                new_word = new_word + words_to_test[x][y]
            if third_value == True and y < len(words_to_test[x + 1]):
                new_word = new_word + words_to_test[x][y]
        new_words_list.append(new_word)
    return new_words_list

def correct_words(words_to_test=list()):
    spell = SpellChecker(language="pt")
    for word in words_to_test:
        if word in spell:
            print(f"This word '{word}' is correct.")
        else:
            # Obtém sugestões de correção
            sugestoes = spell.candidates(word)
            print(f"This word '{word}' is incorrect.")
            print(f"Suggestion for '{word}': {sugestoes}")


correct_words(interconnect_words(list_words))