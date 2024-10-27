import range

number = int(input('A number: '))
x = 2
y = 15

if range.range(x, y, number):
    print(f"Number {number} in the range <{x},{y}>: yes")
else:
    print(f"Number {number} in the range <{x},{y}>: no")