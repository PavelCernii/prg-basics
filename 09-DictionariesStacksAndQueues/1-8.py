price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

total_before = 0 
print('Before discount:')

for item, price in price_list.items():
    print(f"{item}: {price}")
    total_before += price
print(f"Total before discount: {round(total_before, 2)}")


for item in price_list:
    price_list[item] = round(price_list[item] * 0.9, 2)

print("\nPrices after discount:")

total_after = 0

for item, price in price_list.items():
    print(f"{item}: {price}")
    total_after += price
print(f"Total after discount: {round(total_after, 2)}")
