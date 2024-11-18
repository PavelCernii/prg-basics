arr = [15, 8, 31, 47, 2, 19]
i = 0 
total = 0 

while i < len(arr):
    total += arr[i]
    i += 1

mean = total / len(arr)

print(mean)