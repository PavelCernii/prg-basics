hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]

def hotel_list(hotels):
    result = ""
    index = 0
    for hotel in hotels:
        if index > 0:
            result += ", "
        result += hotel["name"]
        index += 1
    return result

def avg_price(hotels):
    total_price = 0
    count = 0
    for hotel in hotels:
        total_price += hotel["price"]
        count += 1
    return round(total_price / count)

krakow_hotels = hotel_list(hotels_in_Krakow)
krakow_avg_price = avg_price(hotels_in_Krakow)

sopot_hotels = hotel_list(hotels_in_Sopot)
sopot_avg_price = avg_price(hotels_in_Sopot)

cheaper_city = "Krakow" if krakow_avg_price < sopot_avg_price else "Sopot"

print(f"Hotels in Krakow: {krakow_hotels}")
print(f"Average hotel price in Krakow: {krakow_avg_price}")
print(f"Hotels in Sopot: {sopot_hotels}")
print(f"Average hotel price in Sopot: {sopot_avg_price}")
print(f"Cheaper hotels in: {cheaper_city}")