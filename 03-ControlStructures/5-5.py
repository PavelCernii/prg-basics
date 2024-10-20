###
# Sums numbers entered by user
#
total_sum = 0
count = 0 
mean = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    count += 1 
    
    mean = total_sum / count

print(f"The total sum of the numbers is: {total_sum}") 
print(f'Arithmetic mean: {mean}')