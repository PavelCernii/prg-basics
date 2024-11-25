with open('it_company.csv', 'r') as file:
    lines = file.readlines()

index = 0 
while index < len(lines):
    for item in lines[index:index+5]:
        print(item)
    index += 5

    if index < len(lines):
        input('Press Enter...')
