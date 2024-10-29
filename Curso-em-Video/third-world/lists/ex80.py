#User vai digitar, 5 números inteiros. Colocar na lista, já na posição correta, sem usar sorted()
#mostrar a lista

numb_list = list()

for x in range(0,5):
    numb = int(input('Enter a number: '))
    
    if x == 0 or numb > numb_list[-1]:
        numb_list.append(numb)
    else:
        pos = 0
        while pos < len(numb_list):
            if numb <= numb_list[pos]:
                numb_list.insert(pos, numb)
                break
            pos += 1

print(numb_list)