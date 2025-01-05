from functools import reduce

numbers = [2,4,6,3,7,5]

sum_even = filter(lambda e: e % 2 == 0, numbers)
print(reduce(lambda x,y: x + y, sum_even))