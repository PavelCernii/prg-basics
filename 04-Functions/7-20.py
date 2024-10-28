def is_prime(num):
    d = 2
    while d * d <= num:
        if num % d == 0:
            return False
        d += 1
    return True

def f(n):
    count = 0  # счетчик для найденных простых чисел
    candidate = 1  # текущее число для проверки на простоту
    
    while count < n:
        candidate += 1
        if is_prime(candidate):
            count += 1
    
    return candidate
