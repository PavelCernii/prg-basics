def f(product_code):
    number = int(product_code[0]) + int(product_code[1]) + int(product_code[2])
    if number % 7 == int(product_code[3]):
        return True
    else:
        return False