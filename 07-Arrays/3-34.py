def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=" ")
        print()

matrix_3 = identity_matrix(3)
matrix_5 = identity_matrix(5)
matrix_8 = identity_matrix(8)

print("3x3 Identity Matrix:")
print_matrix(matrix_3)

print("\n5x5 Identity Matrix:")
print_matrix(matrix_5)

print("\n8x8 Identity Matrix:")
print_matrix(matrix_8)
