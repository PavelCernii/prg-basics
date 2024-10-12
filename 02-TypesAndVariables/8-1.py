###
# Calculation of circle area and circumference 
#
import math
# determine radius and PI values
r = float(input('Enter radius of a circle: '))
pi = math.pi
# calculate area 
s = pi * r**2
# calculate circumference 
circumference = 2 * pi * r
# display results
print(f'Radius = {r}\ncircumference = {round(circumference, 2)}\nArea = {round(s, 2)}')