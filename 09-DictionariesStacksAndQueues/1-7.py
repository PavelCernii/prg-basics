products = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}
total = 0 
for item, value in products.items():
    print(f'{item} : {value}')
    total += value

print('Total number of products in the store:' ,total)

