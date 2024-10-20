hour = int(input('Enter how many hours you was at parking: '))
if hour <= 2:
    print('You should pay 5 PLN')
elif hour <= 6:
    print('You should pay 15 PLN')
else: 
    print('You should pay 20 PLN')  