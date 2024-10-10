amount = float(input("Enter your amount: "))
vat = amount * 0.23

amount = round(amount, 2)
vat = round(vat, 2)


print(f'Amount : {amount}')
print(f'VAT 23% : {vat}')