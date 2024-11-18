import MyArrays

numbers = [7, 3, 8, 5, 2]

print("Numbers:", MyArrays.array_to_string(numbers))
second_largest_num = MyArrays.second_largest(numbers)
print("Second largest number:", second_largest_num)
median_num = MyArrays.median(numbers)
print("Median:", median_num)
min_max_values = MyArrays.min_max(numbers)
print("Smallest and largest number:", min_max_values[0], min_max_values[1])
numbers_as_string = MyArrays.array_to_string(numbers)
print("Numbers as a string:", numbers_as_string)
