###
# Reads the entire contents of a file
#
def read_from_file(name):
   with open(name, 'r') as file:
      content = file.read()
   return content

file_content = read_from_file('countries.txt')

file_lines = sorted(file_content.splitlines())

for line in file_lines:
   print(line)