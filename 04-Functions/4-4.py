# Calculates the sum of the digits in a number



def sum_digits(number):
    number = str(abs(number))    
    digit_sum = 0
    for digit in number:
        digit_sum += int(digit)
    return digit_sum



any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')