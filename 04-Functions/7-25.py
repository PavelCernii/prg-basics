def f(x, y):
    total = 0
    for num in range(x, y + 1):
        if num % 2 == 0 and num % 3 == 0 and num % 4 != 0:
            total += num
    return total

print(f(1, 20))