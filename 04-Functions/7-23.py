def f(password):
    if len(password) < 6:
        return False
    if len(set(password)) != len(password):
        return False
    return True

print(f("A2water3"))