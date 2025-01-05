x = int(input('distance'))
y = int(input('hours'))
z = int(input('minutes'))

def avg_speed(distance,hours,minutes):
    min_to_h = minutes / 60
    speed = distance / (min_to_h + hours)
    return speed

print(f'avg: {avg_speed(x,y,z)}')