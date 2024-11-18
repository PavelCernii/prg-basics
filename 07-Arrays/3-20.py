arr = [7, 9, 2, 4, 5, 6]
even = []
odd = []
for num in arr:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
arr = even + odd
print(arr)
