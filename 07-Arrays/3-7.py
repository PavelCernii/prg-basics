arr = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
long = 0
name = ''

for item in arr: 
    if len(item) > long:
        long = len(item)
        name = item

print(name)