# Section 06: Files in Python

[VOLVER a README.md](README.md)

## Indice

* [Files (Open - read - write)](#files-open---read---write)
* [Copiar archivos](#copiar-archivos)
* [Archivos CSV](#archivos-csv)
* [Archivos JSON](#archivos-json)
* [Usando la sintaxis with - context managers](#usando-la-sintaxis-with---context-managers)
* [Importar nuestros propios archivos](#importar-nuestros-propios-archivos)
* [Relative imports](#relative-imports)


## Files (Open - read - write)

* Modo: read (``'r'``)
```python
my_file = open('data.txt', 'r')
file_content = my_file.read()
my_file.close()

print(file_content)
```

* Modo: write (``'w'``)

```python
user_name = input('Enter your name: ')

my_file_writing = open('data.txt', 'w')
my_file_writing.write(user_name)
my_file_writing.close()
```
>**Nota:** El modo ``w`` sobreescribe el contenido del archivo.

[Video: Files in Python](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445280?start=0)

## Copiar archivos

```python
# Ask the user for a list of 3 friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to 'nearby_friends.txt'

# hint: readlines()

if __name__ == '__main__':

    friends = input('Enter three friend names, separated by commas (no spaces, please): ').split(',')

    people = open('people.txt', 'r')
    people_nearby = [line.strip() for line in people.readlines()]  # [line1, line2, line3, etc]
    people.close()

    friends_nearby_list = [friend for friend in friends if friend.lower() in [person.lower() for person in people_nearby]]

    nearby_friends_file = open('nearby_friends.txt', 'w')

    for friend in friends_nearby_list:
        print(f'{ friend } is nearby! Meet up with them.')
        nearby_friends_file.write(f'{ friend }\n')

    nearby_friends_file.close()

```

[Video: Copiar archivos](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445282?start=0)

## Archivos CSV

```python
file = open('csv_data.txt', 'r')
lines = [line.strip() for line in file.readlines()]  # [line1, line2, line3, etc]
file.close()

lines = lines[1:]

for line in lines:
    person_data = line.split(',')
    name = person_data[0].title()
    age = person_data[1]
    university = person_data[2].capitalize()
    degree = person_data[3].title()

    print(f'{ name } is { age }, studying { degree } at { university }')

# Como crear un row
sample_csv_value = ','.join(['Rolf', '25', 'MIT', 'Computer Science'])
print(sample_csv_value)

```

[Video: Archivos csv](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445284?start=0)

## Archivos JSON

```python
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
```

[Video: Archivos JSON](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445286?start=0)

## Usando la sintaxis with - context managers

```python
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
```
>**NOTA:** los context mamagers pueden ser utilizados para hacer tareas de setup y tear down o para hacer open y close de una base de datos.  
>En los ejemplos de arriba el archivo es cerrado por el context manager una vez que  finaliza la ejecuci'on del bloque ``with``


[Video: Usando with syntax](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445290?start=0)

## Importar nuestros propios archivos

Solo se pueden importar de forma directa los archivos que se encuentran en el directorio base de nuestro proyecto. En caso que se necesite usar un paquete se debe hacer referencia al mismo.
Para decirle a python que un directorio es un paquete se debe crear dentro del mismo un archivo vacio llamado ``__init__.py``  
Al momento de hacer un import python ejecuta el archivo que se esta importando, incluso si solo se importa una función.

* Importar todo el archivo

```python
import utils.file_operations

if __name__ == '__main__':
    utils.file_operations.save_to_file('Rolf','76_data.txt')
```
> **Nota:** Al utilizar las funciones del archivo importado se las debe llamar con su path completo.

* Importar solo algunas funciones
```python
from utils.file_operations import save_to_file, read_file


if __name__ == '__main__':
    save_to_file('Rolf', '76_data.txt')
```
> **Nota:** En este caso no es necesario utilizar el path completo al llamar las funciones. Sin embargo puede llevar a confusiones si se necesitan utilizar funciones que pertenecen a distintos archivos pero que tienen el mismo nombre.

[Video: Importing our own files](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445292?start=0)

## Relative imports

[Video: Relative imports - Childrens](#https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445296?start=0)  
[Video: Relative imports - Parents](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9445298?start=0)
