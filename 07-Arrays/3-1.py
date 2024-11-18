arr = [34,7,19,4,21,8]
n = 0 
i = 0 
while i < len(arr):
    for item in arr:
        if item % 2 == 0:
            n += 1 
        i += 1

print(n)