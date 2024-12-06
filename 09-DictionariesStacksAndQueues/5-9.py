province_dict = {}
with open("province.csv", "r", encoding="utf-8") as province_file:
    next(province_file)
    for line in province_file:
        prefix, province = line.strip().split(",")
        province_dict[prefix] = province

vehicle_count = {province: 0 for province in province_dict.values()}

with open("vehicle.txt", "r", encoding="utf-8") as vehicle_file:
    for registration in vehicle_file:
        registration = registration.strip()
        prefix = registration[0]
        if prefix in province_dict:
            province = province_dict[prefix]
            vehicle_count[province] += 1

for province, count in vehicle_count.items():
    print(f"{province}: {count}")
