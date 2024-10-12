# A program that displays your height both in cm and in feet and inches.
#
cm = int(input('Enter your height in cm: '))

feet = cm // 30.48 
inches = (cm % 30.48) / 2.54  

print(f'I am {cm} cm tall, i.e. {int(feet)} feet and {round(inches, 2)} inches')