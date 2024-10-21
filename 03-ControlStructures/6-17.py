time = input('Enter time (24-hour format): ')
hours_str = time[:2]
minutes_str = time[3:]
hours = int(hours_str)

if hours > 12:
    hours -= 12
    print(f'Time in 12-hour format: {hours}:{minutes_str}pm')
elif hours == 12:
    print(f'Time in 12-hour format: {hours}:{minutes_str}pm')
elif hours == 0:
    print(f'Time in 12-hour format: 12:{minutes_str}am')
else:
    print(f'Time in 12-hour format: {hours}:{minutes_str}am')
