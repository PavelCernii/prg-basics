fibonacci_sequence = [0, 1]

while len(fibonacci_sequence) < 20:
    next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2] 
    fibonacci_sequence += [next_number]  

result = ''
for i in range(len(fibonacci_sequence)):
    result += str(fibonacci_sequence[i]) + ' '

print(result)
