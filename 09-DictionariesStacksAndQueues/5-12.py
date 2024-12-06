import queue

def reversed_str(inp_str):
    stack = queue.LifoQueue()

    for char in inp_str:
        stack.put(char)

    string = ''
    while not stack.empty():
        string += stack.get()

    return string

text = input('input text to reverse: ')
print(reversed_str(text))