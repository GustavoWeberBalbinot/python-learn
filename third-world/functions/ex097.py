#faça uma função, escreva(), que receba um texto, e mostre uma mensagem adaptável.

def escreva(text):
    print('-'* (len(text) + 4))
    print(f'  {text}')
    print('-'* (len(text) + 4))

escreva(str(input('Enter with a text: '.strip())))