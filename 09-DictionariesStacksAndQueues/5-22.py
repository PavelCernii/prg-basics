import json

product = {}

product['name'] = input("Enter the product name: ")
product['price'] = float(input("Enter the product price (real number with two decimal places): "))
paid_input = input("Has the product been paid for? (yes/no): ").lower()

if paid_input == 'yes':
    product['paid'] = True
elif paid_input == 'no':
    product['paid'] = False
else:
    print("Invalid input for payment status. Defaulting to 'no'.")
    product['paid'] = False

with open('product.json', 'w', encoding='utf-8') as file:
    json.dump(product, file, ensure_ascii=False, indent=4)

print("Product data has been saved to product.json")
