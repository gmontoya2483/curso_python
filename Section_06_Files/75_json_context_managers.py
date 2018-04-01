import json

with open('friends_json.txt', 'r') as file:
    file_contents = json.load(file)  # Lee el archivo y lo convierte en un diccionario


print(file_contents['friends'][0])


cars = {'cars': [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'},
    {'make': 'Audi', 'model': 'S3'}
    ]
}

with open('cars.json', 'w') as file:
    json.dump(cars, file)


