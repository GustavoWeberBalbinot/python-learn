'''
Este exercício é uma história com moral sobre um dos erros mais comuns e difíceis de encontrar no Python. Escreva uma definição de classe chamada Kangaroo com os seguintes métodos:

Um método __init__ que inicialize um atributo chamado pouch_contents  em uma lista vazia.

Um método chamado put_in_pouch que receba um objeto de qualquer tipo e o acrescente a pouch_contents.

Um método __str__ que retorne uma representação de string do objeto Kangaroo e os conteúdos de pouch (bolsa).

Teste o seu código criando dois objetos Kangaroo, atribuindo-os a variáveis chamadas kanga e roo, e então acrescentando roo ao conteúdo da bolsa de kanga.

'''



class Kangaroo():

    def __init__(self, pouch_contents=None):
        if pouch_contents is None:
            pouch_contents = [] #It forces Python to create a new list, and create a new list every time, and not combine all lists.
        self.pouch_contents = pouch_contents
    
    def put_in_pouch(self,other):
        self.pouch_contents.append(other)

    def __str__(self):
        values = [str(item) for item in self.pouch_contents] #Passes through every item and transforms it into a list, resolving the problem, where print runs N times for N values
        return f"The object Kangaroo with our pouch: {values}"

kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch(roo)
print(f'ROO:\n{roo}')
print(f'\nKANGA:\n{kanga}')
