required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write"}

has_permissions = required_permissions.issubset(user_permissions)

print(has_permissions)