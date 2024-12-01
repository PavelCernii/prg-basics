import queue

stack = queue.LifoQueue()

stack.put(2)
stack.put(3)
stack.put(7)
stack.put(4)
stack.put(1)
stack.put(9)
stack.put(8)

two_latets_numbers = stack.get() + stack.get()

print(two_latets_numbers)

total = 0
while not stack.empty():
    item = stack.get()
    total += item

print(total)