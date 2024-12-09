#Escreva uma função chamada rotate_word que receba uma string e um número inteiro como parâmetros, e retorne uma nova string que contém as letras da string original rotacionadas pelo número dado.
#Você pode usar a função integrada ord, que converte um caractere em um código numérico e chr, que converte códigos numéricos em caracteres. As letras do alfabeto são codificadas em ordem alfabética, então, por exemplo:

def rotate_word(word='', numb=0):
    new_word = ''
    for letter in word:
        base = ord('A') if letter.isupper() else ord('a')   ##Tive que pegar do chat, para arrumar o alfabeto para aceitar A e a
        numb_actual = (ord(letter) - base) + numb % 26
        new_word += chr(base + numb_actual)
    return new_word

print(rotate_word('cheer',7))


'''
CHATGPT

def rotate_word(word='', numb=0):
    alphabet = 'abcdefghijklmnopqrstuvwxyz' 
    new_word = ''
    for letter in word:
        if letter.isalpha():  # Verifica se é uma letra
            is_upper = letter.isupper()
            base = 'A' if is_upper else 'a'   ##Interesante, aqui temos uma escolha para base, se a letra foir maiscula usa o 'A' e se for minuscula usa o 'a', pois eles tem números diferentes.
            # Calcula a nova posição com rotação cíclica
            numb_actual = (ord(letter) - ord(base) + numb) % 26         #26% para manter dentro do alfabeto, isso tive que copair dele
            new_word += chr(ord(base) + numb_actual)
        else:
            # Mantém caracteres não alfabéticos inalterados
            new_word += letter
    return new_word
'''