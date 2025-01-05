avg_speed = lambda distance,hours,minutes: distance / ((minutes / 60) + hours)

x = int(input('distance'))
y = int(input('hours'))
z = int(input('minutes'))

result = avg_speed(x,y,z)
print(result)
