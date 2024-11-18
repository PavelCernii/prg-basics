arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]
arr3 = []

for item in arr1:
    if item not in arr2:
        arr3.append(item)

print(arr3) 