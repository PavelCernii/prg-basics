import random

number = random.randint(1,6)

sp_number = number == 1 or number == 6
print(f'Dice rolled: {number}\nSpecial number (1 or 6): {sp_number}')