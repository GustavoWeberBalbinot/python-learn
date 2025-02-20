'''
Leia a documentação do método de dicionário setdefault e use-o para escrever uma versão mais concisa de invert_dict.
'''

dict_teste = {'a': 1, 'b': 1, 'c': 2, 'd': 4, 'e': 3, 'f': 4}

def invert_dict(dict_to_invert = dict):
    inverted = dict()
    for x in dict_to_invert.keys():
        value = dict_to_invert.setdefault(x)
        if  value not in inverted:
            inverted[value] = []
        inverted[value].append(x)
    return inverted


print(invert_dict(dict_teste))


'''
CHAT GPT:
def invert_dict(d):
    inverted = {}
    for k, v in d.items():
        inverted.setdefault(v, []).append(k) ##############This [], create the list in dict, enabling the use of APPEND
    return inverted

'''