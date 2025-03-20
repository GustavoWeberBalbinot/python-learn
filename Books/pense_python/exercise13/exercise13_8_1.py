'''
a) Escreva um programa que leia o texto de um arquivo e execute a análise de Markov. O resultado deve ser um dicionário que mapeie prefixos a uma coleção de possíveis sufixos. A coleção pode ser uma lista, tupla ou dicionário; você é que deverá fazer a escolha adequada. Você pode testar seu programa com um comprimento de prefixo 2, mas deve escrever o programa de forma que seja fácil testar outros comprimentos.
'''
words = list()

with open('Books/pense_python/exercise13/file13-7.txt', 'r', encoding='utf-8') as file:
    for x in file:
        x = (x.replace('"', '').replace('(','').replace(')','').split())
        for y in x:
            words.append(y)


def get_pre_su(list_words, lenght = 2):
    d = dict() #CHATGPT HACK -- d = defaultdict(list)  # Inicializa dicionário que cria listas automaticamente
    for x in range(len(list_words) - lenght):
        prefx = tuple(list_words[x:x+lenght])
        if (prefx) not in d:
            d[prefx] = []
        d[prefx].append(list_words[x+lenght])
    return d

if __name__ == "__main__":
    get_pre_su(words)
