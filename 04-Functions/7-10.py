def f(x, y):
    number = 0

    for n in range(x, y):
        if n < 0 and n % 2 == 0:
            number += 1

    return number

print(f(-1, 11))
    