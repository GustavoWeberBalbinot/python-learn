'''
Altere o programa anterior para ler uma lista de palavras (ver “Leitura de listas de palavras”, na página 133) e então exiba todas as palavras do livro que não estão na lista de palavras. Quantas delas são erros ortográficos? Quantas delas são palavras comuns que deveriam estar na lista de palavras, e quantas são muito obscuras?
'''

from exercise13_2 import format_txt, read_archive

my_archive = 'Books/pense_python/exercise13/file13-2.txt'
txt_my_archive = read_archive(my_archive)
all_values_dict = format_txt(txt_my_archive)

with open('Books/pense_python/exercise13/moby_words.txt', 'r', encoding='utf-8') as file:
    txt_moby = file.read()

d = {'exists:': [], 'doesnt exists:': []}

for words in all_values_dict.keys():
    words = str(words).replace('\n', '')
    if words in txt_moby:
        d['exists:'].append(words)
    else:
        d['doesnt exists:'].append(words)

print(f"'EXISTS WORDS:'\n {d['exists:']} \n")
print(f"'DOESNT EXISTS WORDS:'\n  {d['doesnt exists:']}")