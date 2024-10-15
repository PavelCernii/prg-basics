###
# Checking whether a car exceeded the speed limit
#
speed_limit = 140
car_speed = int( input('Enter car speed (km/h): ') )

if car_speed >= speed_limit:
    print(f'Your speed is {speed_limit}km/h')
    print('Warning: speed limit exceeded!!')
else :
    print('All is good!')