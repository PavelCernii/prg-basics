import math

circumference = int(input("Enter tree circumference in cm: "))

diametr = circumference / math.pi
can_be = diametr >= 50
print(f'Tree can be cut down: {can_be}')