'''
Se você baixar minha solução do Exercício 12.2 em http://thinkpython2.com/code/anagram_sets.py, verá que ela cria um dicionário que mapeia uma string ordenada de letras à lista de palavras que podem ser soletradas com aquelas letras. Por exemplo, 'opst' mapeia à lista ['opts', 'post', 'pots', 'spot', 'stop', 'tops'].

Escreva um módulo que importe anagram_sets e forneça duas novas funções: store_anagrams deve guardar o dicionário de anagramas em uma “prateleira” (objeto criado pelo módulo sheve); read_anagrams deve procurar uma palavra e devolver uma lista dos seus anagramas.
'''

import nltk
import dbm
from nltk.corpus import words

word_set = set(words.words())

def exist_word(palavra):
    return palavra.lower() in word_set



def letters_to_anagram(letters):
    if len(letters) == 1:
        return [letters]
    result = []
    for i in range(len(letters)):
        letra_fixa = letters[i]
        restantes = letters[:i] + letters[i+1:]
        for p in letters_to_anagram(restantes):
            result.append([letra_fixa] + list(p))
    return result


def st_anagram(words, letters):
    try:
        db = dbm.open('Books/pense_python/exercise14/dbm_anagram', 'c')
    except Exception as e:
        print(f'This error:\n{e}')
        return
    key = ''.join(sorted(letters)).encode()
    if key in db:
        db.close()
        return
    db[key] = ','.join(words).encode()
    db.close()



def rd_anagram(letters):
    try:
        db = dbm.open('Books/pense_python/exercise14/dbm_anagram', 'c')
    except Exception as e:
        print(f'This error:\n{e}')
        return
    key = ''.join(sorted(letters)).encode()
    if key in db:
        words = db[key].decode().split(',')
        print(f"{letters} → {words}")
    else:
        print(f"No anagrams found for {letters}")
    db.close()



def main(letters,store_anagram = True, read_anagrams = False):
    value = letters_to_anagram(letters)
    words = list()
    for x in value:
        x = str(x)
        x = x.replace('[', '').replace(']', '').replace("'", '').replace('"','').replace(',','').replace(' ','')
        if exist_word(x):
            words.append(x)
    if words == []:
        print(f'This {letters}, not form any word')
        return
    if store_anagram:
        st_anagram(words, letters)
    if read_anagrams:
        rd_anagram(letters)
    print('Ending the program')
    return


if __name__ == "__main__":
    letters = str(input('Enter with the letters: '))
    main(letters,store_anagram=True, read_anagrams=True)



'''
Chatgpt gave me a lot of tips with the dbm, because I have never worked with this function before.

'''