temp_c = int(input('Enter the temperature in Celsius: '))

formula_f = temp_c * 9/5 + 32 
formula_k = temp_c + 273.15

print(f'Temperature in Celsius: {temp_c}\nTemperature in Kelvin: {round(formula_k, 2)}\nTemperature in Fahrenheit: {round(formula_f, 2)}')
