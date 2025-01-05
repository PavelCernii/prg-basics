###
# Calculates arithmetic mean of two integer numbers
#
def mean(x,y):
   a = int(x) + int(y)
   a = a/2
   return a

# takes two numbers from keyboard
n1 = input('Input 1 n:')
n2 = input('Input 2 n:')

# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')