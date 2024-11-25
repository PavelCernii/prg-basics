with open('files.txt', 'r') as file:
    file_names = file.readlines()

for name in file_names:
    name = name.strip()
    if len(name.split('.')[-1]) == 4:
        print(name)
