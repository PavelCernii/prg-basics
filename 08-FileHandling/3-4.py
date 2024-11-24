import re  # module for regular expressions

email_file = 'report.txt'

with open(email_file, 'r') as file:
    email = file.read()

pattern = '\d+'

amounts = re.findall(pattern, email)

total = 0
for amount in amounts:
    total += int(amount) 
    
print(f"Total amount spent: €{total}")
