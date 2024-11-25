with open('powers.txt', 'w') as file:
    for number in range(1, 101):
        second_power = number ** 2
        third_power = number ** 3
        result = f"{number},{second_power},{third_power}\n"
        file.write(result)
        print(result.strip())
