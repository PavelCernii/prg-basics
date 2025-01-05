fillings = [508, 500, 512, 499, 492, 511, 503, 476, 501, 509]

capacity = 500
tolerance = 0.02

min_fill = capacity * (1 - tolerance)
max_fill = capacity * (1 + tolerance)

def is_incorrectly_filled(min_fill, max_fill):
    return lambda fill: fill < min_fill or fill > max_fill

incorrect_bottles = list(filter(is_incorrectly_filled(min_fill, max_fill), fillings))

total_bottles = len(fillings)
incorrect_percentage = (len(incorrect_bottles) / total_bottles) * 100

print("Bottle capacity:    500ml")
print("Filling tolerance:  2%")
print("Filled bottles:     " + ",".join(map(str, fillings)))
print("Incorrectly filled: " + str(int(incorrect_percentage)) + "%")

