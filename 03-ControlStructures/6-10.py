age = int(input("Enter the dog's age in human years: "))
human_age = 0
if age <= 2: 
    human_age = age * 10.5 
elif age > 2:
    human_age = 10.5 * 2 + (age - 2) * 4
    print(f"The dog's age in dog's years is {human_age}")
else:
    print('Something wrong!')