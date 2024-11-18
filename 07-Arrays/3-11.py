def bubblesort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

arr1 = [64, 34, 25, 12, 22, 11, 90]
arr2 = [3, 1, 4, 1, 5, 9, 2, 6]
arr3 = [10, 7, 3, 8, 5, 2]

print("Sorted arr1:", bubblesort(arr1))
print("Sorted arr2:", bubblesort(arr2))
print("Sorted arr3:", bubblesort(arr3))