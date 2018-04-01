

if __name__ == '__main__':

    # Leer el contenido de un archivo de texto (en forma de un único string)

    my_file = open('data.txt', 'r')
    file_content = my_file.read()

    my_file.close()

    print(file_content)

    # Escribir en un archivo de texto

    user_name = input('Enter your name: ')

    my_file_writing = open('data.txt', 'w')  # El modo w sobreescribe el contenido del archivo por lo que se le escriba
    my_file_writing.write(user_name)
    my_file_writing.close()
