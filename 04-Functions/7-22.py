def f(name):
    a = ''
    x = name.split(" ")
    for i in x:
        a += i[0]
    return a

print(f('Internet of Things'))
    