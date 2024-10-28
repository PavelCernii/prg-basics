def f(expression):
    result = 0
    current_number = ""
    sign = 1
    
    for char in expression:
        if char.isdigit():
            current_number += char
        else:
            result += sign * int(current_number)
            current_number = ""
            sign = 1 if char == '+' else -1 

    result += sign * int(current_number)
    
    return result

print(f("2+3-4+5-0"))