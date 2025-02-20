#Há um método de string chamado count, que é semelhante à função em “Loop e contagem”, na página 123. Leia a documentação deste método e escreva uma invocação que conte o número de letras 'a' em ‘banana’.

def count_letter(word, letter):
    count = 0
    for actual_letter in word:
        if actual_letter == letter:
            count += 1
    print(count)

count_letter('pneumoultramicroscopicossilicovulcanoconiótico', 'o')
