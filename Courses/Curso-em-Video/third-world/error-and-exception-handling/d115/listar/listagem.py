def listar():
    arquivo = open('d155dados.txt', 'r')
    conteudo = arquivo.read()
    linhas = conteudo.splitlines()
    print('-='*30)
    print('Lista de nomes:'.center(60))
    for x in range(0, len(linhas), 2):
        print(f'{linhas[x]} {linhas[x+1]:>50}')
    print('-='*30)
