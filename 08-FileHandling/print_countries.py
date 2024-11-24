###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
    i = 0
    for line in file:
        i += 1
        print(i,line, end="")
