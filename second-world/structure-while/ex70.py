#peça nome e o preço de várias peças, deve perguntar se quer continuar. Retorne, total gasto, quantidade com valor maior de 1000, nome do item mais barato

lesser = sum_price = 0
greater = 1000
greater_item = lesser_item = ''
while True:
    item = str(input('Enter a item: '))
    price = int(input('Enter with the price of item: '))
    sum_price += price
    if lesser == 0:
        lesser = price
        lesser_item = item
    if price > lesser:
        lesser = price
        lesser_item = item
    if price <= greater:
        greater = price
        greater_item = item
    choice = str(input('Do you want continue?[Y/N]')).upper()[0]
    if choice in 'N':
        break


print(f'The total spent is: {sum_price}')
print(f'The item with price greater than 1000 is: {greater_item}, if the price {greater}')
print(f'The lesser item is: {lesser_item}, with the cost {lesser}')