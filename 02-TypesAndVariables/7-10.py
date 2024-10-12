###
# A program that enables a user to challenge a computer.
# The computer throws dice. Then, the user then tries to guess
# the number from dice by entering a number from 1 to 6
# from the keyboard. If the user has guessed the number
# from the dice, the computer displays True. Otherwise,
# the computer displays False.
#
import random
# COMPUTER TURN
computer = random.randint(1,6)
# YOUR TURN
you = int(input("Enter your number: "))

win = computer == you

print(f"Computer's number is : {computer}\nYour number is : {you}\nYou won : {win}")