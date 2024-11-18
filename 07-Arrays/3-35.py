def transpose_matrix(m):
    num_columns = max(len(row) for row in m)  # Find the maximum number of columns
    return [[m[j][i] if i < len(m[j]) else None for j in range(len(m))] for i in range(num_columns)]

def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=" ")
        print()

matrix_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]

matrix_3 = [
    [5, 6, 7, 8]
]

transposed_1 = transpose_matrix(matrix_1)
transposed_2 = transpose_matrix(matrix_2)
transposed_3 = transpose_matrix(matrix_3)

print("Transposed Matrix 1:")
print_matrix(transposed_1)

print("\nTransposed Matrix 2:")
print_matrix(transposed_2)

print("\nTransposed Matrix 3:")
print_matrix(transposed_3)
