my_tuple = (50, 20, 40, 50, 30, 50)
value = int(input("Enter a value to count: "))
count = my_tuple.count(value)
a = ''
for item in my_tuple:
    a += str(item) + ' '
print('Tuple:', a)
print("Value:", value)
print("Number of occurrences:", count)