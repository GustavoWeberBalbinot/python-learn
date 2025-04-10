'''
Em uma grande coleção de arquivos MP3 pode haver mais de uma cópia da mesma música, guardada em diretórios diferentes ou com nomes de arquivo diferentes. A meta deste exercício é procurar duplicatas.

Escreva um programa que procure um diretório e todos os seus subdiretórios, recursivamente, e retorne uma lista de caminhos completos de todos os arquivos com um dado sufixo (como .mp3). Dica: os.path fornece várias funções úteis para manipular nomes de caminhos e de arquivos.

Para reconhecer duplicatas, você pode usar md5sum para calcular uma “soma de controle” para cada arquivo. Se dois arquivos tiverem a mesma soma de controle, provavelmente têm o mesmo conteúdo.

Para conferir o resultado, você pode usar o comando Unix diff.
'''

import os, hashlib

my_dir = 'Books/pense_python/exercise14'

def search_archives(actual_dir,count = 0):
    d_root = dict()
    d_dirs = dict()
    d_file = dict()
    for root, dirs, files in os.walk(actual_dir):
        count += 1
        d_root[count] = root
        d_file[count] = files
        if dirs:
            d_dirs[count] = dirs
            for x in dirs:
                l_root, l_dirs,l_files = search_archives(os.path.join(actual_dir, x), count)
                d_root.update(l_root)
                d_dirs.update(l_dirs)
                d_file.update(l_files)
        else:
            continue
    return d_root, d_dirs, d_file


def check_same_file(my_root,my_file):
    d_hashs = dict()
    for key, value in my_root.items():
        for v in my_file[key]:
            md5_hash = hashlib.md5()
            with open(os.path.join(value, v), 'rb') as f:
                while chunk := f.read(4096):
                    md5_hash.update(chunk)
            md5_hash_hex = md5_hash.hexdigest()
            if md5_hash_hex not in d_hashs:
                d_hashs[md5_hash_hex] = []
            d_hashs[md5_hash_hex].append(v)
    return d_hashs

if __name__ == "__main__":
    my_root, my_dirs, my_file = search_archives(my_dir)
    hash_values = check_same_file(my_root,my_file)
    print(hash_values)