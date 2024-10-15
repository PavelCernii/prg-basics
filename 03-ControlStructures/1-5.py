##
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
#
total_tasks = int(input('Enter total tasks: '))
tasks_ok = total_tasks / 2 
your_tasks = int(input('Enter how many correct tasks you have: '))

if your_tasks > tasks_ok :
    print('You passed!')
else : 
    print('Unfortunately, you failed the test.')