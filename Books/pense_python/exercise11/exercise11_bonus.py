#Como exercício, use o get para escrever a função histogram de forma mais concisa. Tente eliminar a instrução if.

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0) + 1
    return d

print(histogram('brontosaurus'))
