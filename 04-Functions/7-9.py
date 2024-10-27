def f(number, even):
    sum_digits = 0

    for char in str(number):
        digit = int(char)

        if even == True:
            if digit % 2 == 0:
                sum_digits += digit
        else:
            if digit % 2 == 1:
                sum_digits += digit

    return sum_digits

print(f(3124, False))