###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
is_bonus = int(input('Does the employee has bonus? (1 - Yes,2 - No): ')) # does the employee receive a bonus
bonus = 0.3 # 15%

if is_bonus == 1:
    total_salary = basic_salary + basic_salary * bonus
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {"Yes" if is_bonus == 1 else "No"}')
print(f'Total salary: {total_salary}')