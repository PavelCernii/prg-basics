def f(product_code):

    first_three_sum = int(product_code[0]) + int(product_code[1]) + int(product_code[2])
    
    control_digit = first_three_sum % 7

    return control_digit == int(product_code[3])


print(f("2035"))
print(f("7071"))