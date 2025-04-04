import nltk
from nltk.corpus import words


# Função para verificar se a palavra existe no dicionário do NLTK
def palavra_existe(palavra):
    return palavra.lower() in words.words()

# Testando a função
palavra = "example"
if palavra_existe(palavra):
    print(f"A palavra '{palavra}' existe no dicionário.")
else:
    print(f"A palavra '{palavra}' não existe no dicionário.")
