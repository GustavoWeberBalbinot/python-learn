'''
Aqui está outro quebra-cabeça do programa Car Talk (http://www.cartalk.com/content/puzzlers):

“Estava dirigindo outro dia e percebi algo no hodômetro que chamou a minha atenção. Como a maior parte dos hodômetros, ele mostra seis dígitos, apenas em milhas inteiras. Por exemplo, se o meu carro tivesse 300.000 milhas, eu veria 3-0-0-0-0-0.

“Agora, o que vi naquele dia foi muito interessante. Notei que os últimos 4 dígitos eram um palíndromo; isto é, podiam ser lidos da mesma forma no sentido correto e no sentido inverso. Por exemplo, 5-4-4-5 é um palíndromo, então no meu hodômetro poderia ser 3-1-5-4-4-5.

“Uma milha depois, os últimos 5 números formaram um palíndromo. Por exemplo, poderia ser 3-6-5-4-5-6. Uma milha depois disso, os 4 números do meio, dentro dos 6, formavam um palíndromo. E adivinhe só? Um milha depois, todos os 6 formavam um palíndromo!

“A pergunta é: o que estava no hodômetro quando olhei primeiro?”

Escreva um programa Python que teste todos os números de seis dígitos e imprima qualquer número que satisfaça essas condições.
'''

teste_numbs = [
    '3-6-5-5-6-3', #Palindrome 6
    '1-2-4-4-2-5', #Middle palindrome 4
    '1-2-3-1-1-6', #Not is palindrome
    '1-2-2-2-1-5', #Start palindrome 5
    '5-1-2-2-2-1',  #End palindrome 5
    '5-1-2-1-3-4', #Start-Middle palindrome 3
]


def inverse(txt = str()):
    txt = txt[::-1]
    return txt

#Yes, I know this could have all been done in a single function, and increase the value of For and X respectively in it, but this way it becomes more "interesting" 
def analitic_palindrome(palindrome = str(),for_value = int(),x_value = int()):
    '''
    Analitic the palindrome(6 value) in pieces
    Parameters:
    palindrome = value to analitic
    for_value = value to put in for to get N pieces to analitic de palindrome. (2 = Analitic 5; 3 = Analitic = 4; 4 = Analitic 3)
    x_value = value to analitic the piecces on the palindrome(1 = Analitic 5; 2 = Analitic 4; 3 = Analitic 3)
    '''
    for x in range(0,for_value):#Analitic 5 numbs to check palindrome
        range_to = len(palindrome) - x_value + x
        inverse_numb = inverse(palindrome[x:range_to])
        if palindrome[x:range_to] == inverse_numb:
            return True
    return False

def have_palindrome(numb = str()):  #Principal Function
    new_numb = numb.replace('-','')
    if new_numb == new_numb[::-1]: #Analitic 6 numbs to check palindrome
      #  print(numb)
        return True
    if analitic_palindrome(new_numb,2,1):
      #  print(numb)
        return True
    if analitic_palindrome(new_numb,3,2):
     #   print(numb)
        return True
    if analitic_palindrome(new_numb,4,3):
  #      print(numb)
        return True
    return False



'''for a in teste_numbs:
    have_palindrome(a)
'''

list_to_palindrome_numbs = []

for first in range(0,10): #1 to 999999 - in 999999 numbs have 365680 palindromes
    for second in range(0,10):
        for third in range(0,10):
            for fourth in range(0,10):
                for fifth in range(0,10):
                    for sixth in range(0,10):
                        value = f'{first}-{second}-{third}-{fourth}-{fifth}-{sixth}'
                        if have_palindrome(value):
                            list_to_palindrome_numbs.append(value)

print(list_to_palindrome_numbs)
print()
print(len(list_to_palindrome_numbs))


'''
Chatgpt FOR
list_to_palindrome_numbs = []

for num in range(10**6):  # Vai de 000000 a 999999
    digits = [num // 10**i % 10 for i in range(5, -1, -1)]  # Extrai os dígitos
    value = '-'.join(map(str, digits))  # Formata como string
    if have_palindrome(value):
        list_to_palindrome_numbs.append(value)
'''