arr = [15 ,38, 7 ,23 ,14]
num = int(input('Enter a number: '))

def occurs(number, array):
    if array.count(number):
        print(f'Number {number} appears in the array')
    else:
        print(f'Number {number} not appears in the array')
        
occurs(num,arr)

