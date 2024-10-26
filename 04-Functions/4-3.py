###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

def triangle_area(a,b,c):
    p = 0.5*(a + b + c)
    area = math.sqrt(p*(p - a)*(p - b)*(p - c))
    return area

result = triangle_area(a,b,c)

print(f'The area of ​​a triangle with sides {a,b,c} is {result}')
