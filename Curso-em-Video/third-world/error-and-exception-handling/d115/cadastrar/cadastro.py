def cadastrar_validacao(nome, idade):
    while True:
        try:
            idade = int(idade)
            break
        except(ValueError, TypeError):
            print('Erro')
            idade = str(input('Tente digitar a idade novamente: '))
        except(KeyboardInterrupt):
            idade = 0
            print(f'Usuário não digitou nada, valor assumido é 1:')
    cadastrar(nome,idade)

def cadastrar(nome,idade):
    arquivo = open('d155dados.txt', 'a')
    arquivo.write(f'{nome}\n')
    arquivo.write(f'{idade}\n')
    arquivo.close()
