###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = float(input('Enter first number: '))
number2 = float(input('Enter second number: '))
operator = input('Enter the operator (+, -, *, /): ')

if operator == '+':
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    result = number1 / number2
else: 
    print('Something is wrong...')
print(f'{number1} {operator} {number2} = {result}')