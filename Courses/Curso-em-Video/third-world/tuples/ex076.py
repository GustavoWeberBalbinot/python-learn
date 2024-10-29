#tupla com nome de produtos e seus preços.
#mostre os dados em forma tabular.

itens_tuple = (('Milk', '5.00'), ('Beans', '9.99'), ('Rice', '23.00'), ('Chocolate', '99.99'))

print('-'*30)
for x in range(0, len(itens_tuple)):
    print(f'{itens_tuple[x][0].ljust(15)} \t{itens_tuple[x][1]:}')

print('-'*30)
