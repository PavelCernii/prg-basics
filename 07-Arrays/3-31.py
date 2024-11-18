arr = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

min_value = arr[0][0]
max_value = arr[0][0]
min_pos = (0, 0)
max_pos = (0, 0)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] < min_value:
            min_value = arr[i][j]
            min_pos = (i, j)
        if arr[i][j] > max_value:
            max_value = arr[i][j]
            max_pos = (i, j)

print(f"Smallest value: {min_value} at row {min_pos[0]}, column {min_pos[1]}")
print(f"Largest value: {max_value} at row {max_pos[0]}, column {max_pos[1]}")
