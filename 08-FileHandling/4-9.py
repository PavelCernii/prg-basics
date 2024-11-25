import csv

def print_graphic_designers(filename):
    print("GRAPHIC DESIGNERS")
    print("=================")
    
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Job Title'] == 'Graphic Designer':
                print(f"{row['First Name']} {row['Last Name']},{row['Email']}")

print_graphic_designers('it_company.csv')
