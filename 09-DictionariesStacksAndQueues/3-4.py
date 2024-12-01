import queue

def convert_to_binary(number):
    stack = queue.LifoQueue()

    while number > 0: 
        reminder = number % 2 
        stack.put(reminder)
        number = number // 2

    binary_number = ""
    while not stack.empty():
        binary_number += str(stack.get())

    return binary_number

number = int(input("Enter a natural number: "))

binary_number = convert_to_binary(number)

print(f"Natural number: {number}")
print(f"Binary number: {convert_to_binary(number)}")


