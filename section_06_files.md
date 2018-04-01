# Section 06: Files in Python

[VOLVER a README.md](README.md)

## Indice

* [Files (Open - read - write)](#files-open---read---write)
* [Copiar archivos](#copiar-archivos)
* [Archivos CSV](#archivos-csv)

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


