import csv

def print_low_price_low_stock(filename):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            price = float(row['Price'])
            stock = int(row['Stock_Quantity'])
            if price < 60 and stock < 40:
                print(f"{row['Product_Name']}, {row['Category']}, {row['Size']}, {row['Color']}, {row['Price']}, {row['Stock_Quantity']}")

print_low_price_low_stock('clothing.csv')
