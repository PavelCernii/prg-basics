def f(number):
    num_str = str(number)
    sum_repeated = 0
    
    for digit in '0123456789':
        count = num_str.count(digit)
        if count > 1:
            sum_repeated += int(digit) * count
    
    return sum_repeated

print(f(1027))
print(f(230335))
print(f(513553007))
