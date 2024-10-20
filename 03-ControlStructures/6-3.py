###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#

light_switch1 = False # False - switch off, True - switch on
light_switch2 = False
bulbs_on = 0

light_switch1 = input('Is the first switch on? (1 - Yes, 2 - No): ')
light_switch2 = input('Is the second switch on? (1 - Yes, 2 - No): ')

if light_switch1 == '1':
    bulbs_on += 1
if light_switch2 == '1':
    bulbs_on += 2
    
print("Number of bulbs lit:", bulbs_on)