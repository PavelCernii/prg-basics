original_tuple = (10, 20, 30, 40, 50)

print("Tuple:", end="")
for i in original_tuple:
    print(f",{i}", end="")
print()

print("Reverse order:", end="")
for i in original_tuple[::-1]:
    print(f",{i}", end="")
