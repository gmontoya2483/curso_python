# Section 06: Files in Python

[VOLVER a README.md](README.md)

## Indice

* [Files (Open - read - write)](#files-open-read-write)
*

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