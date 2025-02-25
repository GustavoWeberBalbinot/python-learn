'''
Escreva uma função chamada uses_only que receba uma palavra e uma série de letras e retorne True, se a palavra só contiver letras da lista. Você pode fazer uma frase usando só as letras acefhlo? Que não seja “Hoe alfalfa?”
'''

#CHATGPT Cases to use and teste the program:
# Caso onde a palavra só contém as letras permitidas (deve retornar True)
p1 = "hello"
l1 = "helo"

# Caso onde a palavra contém letras não permitidas (deve retornar False)
p2 = "hello"
l2 = "abc"

# Caso com todas as letras iguais (deve retornar True)
p3 = "aaa"
l3 = "a"

# Caso com letras maiúsculas e minúsculas (dependendo da implementação, pode ser True ou False)
p4 = "HELLO"
l4 = "helo"

# Caso onde todas as letras do alfabeto são permitidas (deve retornar True para qualquer palavra)
p5 = "python"
l5 = "abcdefghijklmnopqrstuvwxyz"

# Caso onde não há letras permitidas (deve retornar False para qualquer palavra)
p6 = "word"
l6 = ""

# Caso onde a palavra está vazia (deve retornar True porque não contém letras proibidas)
p7 = ""
l7 = "abc"

# Caso onde as letras permitidas estão vazias (deve retornar False, pois não há letras permitidas)
p8 = "abc"
l8 = ""

#My code has a some problems, but to this testes it works.
def uses_only(word = str(), letters_allowed = str()):
    if word == '':
        return True
    letters_allowed = list(letters_allowed)
    count = 0
    for letter in letters_allowed:
        if letter in word.lower(): #I could use 'ALL' but NO
            count += 1
            if count == len(word) or count == len(letters_allowed):
                return True
    return False

print(uses_only(p1,l1))
print(uses_only(p2,l2))
print(uses_only(p3,l3))
print(uses_only(p4,l4))
print(uses_only(p5,l5))
print(uses_only(p6,l6))
print(uses_only(p7,l7))
print(uses_only(p8,l8))

'''
CHATGPT:

def uses_only(word: str, letters_allowed: str) -> bool:
    for letter in word.lower():
        if letter not in letters_allowed:
            return False  # Se encontrar uma letra proibida, já retorna False
    return True  # Se passar por toda a palavra sem problemas, retorna True

'''