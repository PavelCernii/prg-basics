import re

# read username and password from keyboard
username = input("Enter username: ")
password = input("Enter password: ")

# pattern (criteria) for username and password
username_pattern = r'^[A-Za-z]{6,}$'  # Username must be at least 6 characters long and only lowercase letters
password_pattern = r'^[A-Za-z0-9_]{8,}$'  # Password must be at least 8 characters long and contain letters, numbers, and underscores

# check if username and password match the patterns
username_match = re.match(username_pattern, username)
password_match = re.match(password_pattern, password)

# print results
if username_match and password_match:
    print("Username and password are valid.")
else:
    print("Username or password is invalid.")
