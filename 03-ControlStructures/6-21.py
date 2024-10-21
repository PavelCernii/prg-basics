amount = int(input('Enter rhe amount in PLN: '))

pln_5 = amount // 5
remaining = amount % 5

pln_2 = remaining // 2 
remaining = remaining % 2 

pln_1 = remaining 

print(f'The amount of PLN {amount} in coins: ')
print(f'5 PLN coins :{pln_5}')
print(f'5 PLN coins :{pln_2}')
print(f'5 PLN coins :{pln_1}')