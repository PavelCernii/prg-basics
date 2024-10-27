def f (number1,number2,operator):
    if operator == '+':
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == '*':
        result = number1 * number2
    elif operator == '%':
        result = number1 % number2
    elif operator == '**':
        result = number1 ** number2
    
    return result

print(f(2,3, "**"))