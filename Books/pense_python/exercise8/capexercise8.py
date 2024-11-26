

def find(word, letter, index = 0):
    for x in range(index,len(word)):
        if word[x] == letter:
            return x
    return -1


print(find('banana', 'a', 3))