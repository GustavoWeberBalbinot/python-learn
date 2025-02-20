#Leia a documentação dos métodos de strings em http://docs.python.org/3/library/stdtypes.html#string-methods. Pode ser uma boa ideia experimentar alguns deles para entender como funcionam. strip e replace são especialmente úteis.

#strip (retira todos os espaços antes do inicio e depois do final)
#rstrip (retira apenas os espaços a direita, ou seja, no final)
#lstrip (retira apenas os espaços a esquerda, ou seja, no inicio)

phrase_test = '   this phrase is a test    '
phrase_test_strip = phrase_test.strip()
rphrase_test = phrase_test.rstrip()
lphrase_test = phrase_test.lstrip()

print('|', phrase_test_strip, '|')
print('|', rphrase_test, '|')
print('|', lphrase_test, '|')

phrase_test_replace = phrase_test.replace(' ', '*')
print(phrase_test_replace)