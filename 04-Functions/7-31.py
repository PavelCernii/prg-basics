def power(x, n):
    if n == 0:
        return 1
    elif n > 0:
        n = x * x**(n-1)
        return n 
    
print(power(2, 4))
