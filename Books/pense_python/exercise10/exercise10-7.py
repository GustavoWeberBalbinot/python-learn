'''
Escreva uma função chamada has_duplicates que tome uma lista e retorne True se houver algum elemento que apareça mais de uma vez. Ela não deve modificar a lista original.
'''

t1 = [1, 2, 3, 4, 5, 1]
t2 = ['apple', 'banana', 'cherry', 'apple']
t3 = ['apple', 'banana', 'cherry']

def has_duplicates(t):
    list_test = []
    for itens in t:
        if itens in list_test:
            return True
        list_test.append(itens)
    return False

print(has_duplicates(t3))
#My code with the time complexy is O(n2)
#Code the CHATGPT with the time complexy is O(n) (I didnt knew about SET)

'''
def has_duplicates(t):
    seen = set() ### The set function, keep the value and dont let it put repeat items
    for item in t:
        if item in seen:
            return True
        seen.add(item) #Add items in ''Set''
    return False

# Testes
t1 = [1, 2, 3, 4, 5, 1]
t2 = ['apple', 'banana', 'cherry', 'apple']
t3 = ['apple', 'banana', 'cherry']

print(has_duplicates(t1))  # True
print(has_duplicates(t2))  # True
print(has_duplicates(t3))  # False
'''