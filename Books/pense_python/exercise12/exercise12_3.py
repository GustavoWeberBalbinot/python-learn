'''
Duas palavras formam um “par de metátese” se você puder transformar uma na outra trocando duas letras, por exemplo, “converse” e “conserve”. Escreva um programa que descubra todos os pares de metátese no dicionário. Dica: não teste todos os pares de palavras e não teste todas as trocas possíveis.
'''

#Omg my code is so ugly

word_list = [
    "azeda", "azedo",
    "bird", "brid",
    "horse", "hros",
    "third", "thrid",
    "wasp", "waps",
    "pretty", "purty"
]

def metatese(words = list()):
    t = tuple(words)
    d = dict()
    di = dict()
    count = 0
    for x in range(len(t)):
        if t[x] in d or x == len(t)-1:
            break
        word = t[x]
        next_word = t[x+1]
        for y in range(len(word)):
            list_word = list(word)
            for z in range(len(word)):
                actual_letters = (word[y], word[z], y, z)
                inverse_actual_letters = (word[z], word[y], z, y)
                if inverse_actual_letters in di.values(): #Prevent unnecessary repetion
                    break
                #Switching the characters
                letters = list_word[:]
                letters.pop(z)
                letters.insert(z,actual_letters[0]) 
                letters.pop(y)
                letters.insert(y,actual_letters[1])
                #
                actual_word = str(letters).replace("'",'').replace(',','').replace('[','').replace(']','').replace(' ','')#"Convert the list in str" 
                if actual_word == next_word:
                    d[word] = [actual_word]
                di[count] = actual_letters
                count += 1
        if y == len(word) - 1: #This part is related Prevent unnecessary repetion
            di = dict()
            count = 0
    return d
                
                
print(metatese(word_list))
