arr = [-15, 8, -31, 47, -2, 19]
max_num = 0
min_num = 0 

for item in arr: 
    if item > max_num:
        max_num = item
    if item < min_num:
        min_num = item

print(max_num)
print(min_num)