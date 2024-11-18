arr = [10.5, 20.3, 7.8, 15.6, 25.1, 3.2, 18.9]
value = float(input("Enter a value: "))
count = 0
for num in arr:
    if num > value:
        count += 1
print(count)
