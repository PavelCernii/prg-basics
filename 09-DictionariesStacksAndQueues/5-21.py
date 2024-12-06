import json

favorite_movie = {
    "title": "Inception",
    "director": "Christopher Nolan",
    "year": 2010,
    "genre": "Sci-Fi",
    "rating": 8.8
}

with open('favourite.json', 'w', encoding='utf-8') as file:
    json.dump(favorite_movie, file, ensure_ascii=False, indent=4)

print("Data has been written to favourite.json")
