###
# A program that calculates the number of characters
# of your name, surname and full name
#
name = 'Pavel'  
surname = 'Cernii'

print(f'Your name has {len(name)} characters')
print(f'Your surname has {len(surname)} characters')
print(f'Your full name has {len(name + " " + surname)} characters') # with a space between name and surname