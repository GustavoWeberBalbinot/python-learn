#Um tamanho de passo -1 atravessa a palavra de trás para a frente, então a fatia [::-1] gera uma string invertida. Use isso para escrever uma versão de uma linha de is_palindrome do Exercício 6.3.

def is_palindrome(word = ''):
    word = word.replace(' ', '')
    if word == word[::-1]:
        return True
    else:
        return False

print(is_palindrome('subi no onibus'))
