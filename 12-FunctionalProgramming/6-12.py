medal_data = [
    {"country": "Denmark", "gold": 2, "silver": 4, "bronze": 6},
    {"country": "Finland", "gold": 5, "silver": 0, "bronze": 4},
    {"country": "USA", "gold": 12, "silver": 5, "bronze": 11},
    {"country": "Peru", "gold": 0, "silver": 1, "bronze": 7}
]

at_least_10 = filter(lambda x: x["gold"] + x["silver"] + x["bronze"] >= 10, medal_data)

for country in at_least_10:
    print(f"{country['country']}: {country['gold']},{country['silver']},{country['bronze']}")
