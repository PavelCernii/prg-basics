number_of_product = int(input('Number of products purchased: '))
price = int(input('Enter product price: '))

if number_of_product <= 2:
    print(f'Product price: {price}')
    print(f'Amount to pay: {number_of_product * price}')
elif number_of_product > 2: 
    full_price = 2 * price
    second_price = ((number_of_product - 2) * price) * 0.75
    print(f'Product price: {price}')
    print(f'Amount to pay: {full_price + second_price}')