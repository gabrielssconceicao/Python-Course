import json

file_path = "aula11.json"

person = {
    "name": "John",
    "lastName": "Doe",
    "addresses": [
        {"street": "R1", "number": 32},
        {"street": "R2", "number": 55},
    ],
    "height": 1.8,
    "favorite_numbers": (2, 4, 6, 8, 10),
    "old": True,
    "nothing": None
}

with open(file_path, "w", encoding="utf-8") as file:
    json.dump(
        person,
        file,
        ensure_ascii=False,
        indent=2)
    
with open(file_path, "r", encoding="utf-8") as file:
    p = json.load(file)
    print(p)