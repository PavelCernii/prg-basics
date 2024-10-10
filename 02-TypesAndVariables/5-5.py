price = float(input("Enter price : "))
discount = float(input("Enter discount %: "))

discounted_price = price - (price * discount / 100)
reduction = price - discounted_price

print(f'Price with discount: {round(discounted_price, 2)}')
print(f'Reduction: {round(reduction, 2)}')