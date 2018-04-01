import json

# Leer un archivo JSON (load). Json file a Diccionario
file = open('friends_json.txt', 'r')
file_contents = json.load(file)  # Lee el archivo y lo convierte en un diccionario
file.close()

print(file_contents['friends'][0])


# Escribir en un archivo Json (dump). Diccionario a Json file
cars = {'cars': [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'},
    {'make': 'Audi', 'model': 'S3'}
    ]
}

file = open('cars.json', 'w')
json.dump(cars, file)
file.close()

# Convertir un string Json en un Diccionario (loads). Json string a Diccionario

my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'
cars_dictionary = json.loads(my_json_string)
print(cars_dictionary[0])

# Convertir un diccionario a un string Json (dumps). Diccionario a Json String

cars_dictionary = {'cars': [
    {'make': 'Mercedes Benz', 'model': 'A120'},
    {'make': 'Audi', 'model': 'Q7'}
]}

json_string = json.dumps(cars_dictionary)
print(json_string)







