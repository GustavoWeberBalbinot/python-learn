#Calcule o valor a ser pago em um produto, demonstrando seu preço normal, e a condição de pagamento:
#a vistá dinheiro 10% desconto
#a vistá cartão 5% desconto
#em 2x preço normal
#em 3x ou mais 20% de juros

product_value = float(input('Enter the value of a product: '))
print('Select your method of payment:')
print('1 - Cash on sight')
print('2 - Card on sight')
print('3 - Parcel ')
method_payment = int(input('Enter with your choice: '))
if method_payment == 1:
    print(f'The price was {product_value}, the new price is: {product_value+(product_value*0.1)}')
elif method_payment == 2:
    print(f'The price {product_value}, the new price is: {product_value+(product_value*0.05)}')
elif method_payment == 3:
    parcel = int(input('Enter with your parcel: '))
    price = product_value + (product_value*0.2)
    if parcel <=2 and parcel > 0 :
        print(f'The price is normal: {product_value}, in 2 parcels is: {product_value/2}')
    else:
        print(f'The price {product_value}, the new price is: {price}, in {parcel} parcels is: {price/parcel:.2f}')
else:
    print('The choice was not found')
