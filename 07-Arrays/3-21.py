arr1 = [1, 2, 3]
arr2 = [3, 2, 1, 4, 5]
is_subset = True
for item in arr1:
    if item not in arr2:
        is_subset = False
        break
print(is_subset)
