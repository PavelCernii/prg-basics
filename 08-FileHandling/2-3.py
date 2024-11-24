###
# Makes a copy of a text file
#

# file names
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

# read the content of the original file
with open(original_file) as file:
   content = file.read()

with open(target_file, 'w') as file:
    file.write(content)