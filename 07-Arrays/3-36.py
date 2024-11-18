def flatten_2d_array(arr):
    return [elem for row in arr for elem in row]

def print_array(arr):
    for num in arr:
        print(num, end=" ")
    print()

matrix_1 = [
    [2, 3],
    [1, 5]
]

matrix_2 = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]

matrix_3 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]

flattened_1 = flatten_2d_array(matrix_1)
flattened_2 = flatten_2d_array(matrix_2)
flattened_3 = flatten_2d_array(matrix_3)

print("Flattened Matrix 1:")
print_array(flattened_1)

print("\nFlattened Matrix 2:")
print_array(flattened_2)

print("\nFlattened Matrix 3:")
print_array(flattened_3)
