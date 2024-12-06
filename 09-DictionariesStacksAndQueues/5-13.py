import queue

def f(expression):
    q = queue.Queue()
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            q.put(int(token))
        elif token == '+':
            b = q.get()
            a = q.get()
            q.put(a + b)
        elif token == '-':
            b = q.get()
            a = q.get()
            q.put(a - b)
        elif token == '*':
            b = q.get()
            a = q.get()
            q.put(a * b)
        elif token == '/': 
            b = q.get()
            a = q.get()
            q.put(a / b)

    return q.get()

print(f("2 3 +"))
print(f("2 6 + 4 5 - +"))
print(f("11 7 + 15 - 14 +"))
print(f("2 3 * 4 5 * +"))
print(f("8 4 / 2 *"))
