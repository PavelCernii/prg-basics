import math

height_beach = float(input("Введите ваш рост в метрах (стоя на пляже): "))
distance_beach = 3.57 * math.sqrt(height_beach)
print(f"Расстояние до горизонта с пляжа: {distance_beach:.2f} км")


height_hotel_window = 20
distance_hotel_window = 3.57 * math.sqrt(height_hotel_window)
print(f"Расстояние до горизонта из окна отеля на высоте 20 метров: {distance_hotel_window:.2f} км")
