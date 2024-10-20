current_price = int(input('Enter current price: '))
previous_price = int(input('Enter previous price: '))

price_reduction = ((previous_price - current_price) / previous_price) * 100

if price_reduction >= 10:
    print('Buy the product!!')
    print(f'Product price reduced by {price_reduction}%')
else:
    print('The price has not decreased enough to buy')
    print(f'Product price reduced by {price_reduction}%')