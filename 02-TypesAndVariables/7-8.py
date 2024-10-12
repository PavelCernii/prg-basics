###
# A program that displays results of three dice rolls
# and the sum of dice rolled.
#
import random
dice_roll_1 = random.randint(1,6)
dice_roll_2 = random.randint(1,6)
dice_roll_3 = random.randint(1,6)
total = dice_roll_1 + dice_roll_2 + dice_roll_3
print(f'First dice roll - {dice_roll_1}\nSecond dice roll - {dice_roll_2}\nThird  dice roll - {dice_roll_3}\nSum = {total}')