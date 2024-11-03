def f(text):
    result = ''
    for char in text:
        result += char + '-'
    return result[0:-1]


print(f("Univesity"))