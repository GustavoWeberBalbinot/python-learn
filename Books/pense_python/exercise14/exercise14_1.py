'''
Escreva uma função chamada sed que receba como argumentos uma string-padrão, uma string de substituição e dois nomes de arquivo; ela deve ler o primeiro arquivo e escrever o conteúdo no segundo arquivo (criando-o, se necessário). Se a string-padrão aparecer em algum lugar do arquivo, ela deve ser substituída pela string de substituição.

Se ocorrer um erro durante a abertura, leitura, escrita ou fechamento dos arquivos, seu programa deve capturar a exceção, exibir uma mensagem de erro e encerrar.
'''

file1 = 'Books/pense_python/exercise14/file14_1_1.txt'
file2 = 'a'

def sed(sd_string,rp_string,file1,file2):
    local_archive = 'Books/pense_python/exercise14/' + file2 + '.txt'
    try:
        file2 = open(local_archive,'w')
    except Exception as e:
        print(f'The error is {e}')
        print('Ending the program.')
    with open(file1, 'r', encoding='utf-8') as file:
        for line in file:
            new_line = line.replace(sd_string, rp_string)
            file2.write(new_line)
    file2.close()

    

sed('girafa','cavalo',file1,file2)
