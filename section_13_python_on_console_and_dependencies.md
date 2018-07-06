# Section 13: Python on the console and managing project dependencies

[VOLVER a README.md](README.md)

## Indice

* [Introduction to this section](#introduction-to-this-section)
* [Running python from your console](#running-python-from-your-console)
* [What is a virtualenv](#what-is-a-virtualenv)
* [Navigating the terminal and using virtualenv](#navigating-the-terminal-and-using-virtualenv)
* [Usando Pipenv](#uUsando-pipenv)


## Introduction to this section

[Video: Introduction to this section](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9548082?start=0)

## Running python from your console


1. Open the console:
    
   * On Windows: ``cmd.exe``
   * On Mac: ``Terminal.app``
   * On Linux: ``Terminal``

2. Open the Python console by typing ``python``

    ```console
    Microsoft Windows [Version 6.1.7601]
    Copyright (c) 2009 Microsoft Corporation.  All rights reserved.
    
    C:\Users\montoya>python
    Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)]
     on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```

3. Run any Python command:

    ```console
    Microsoft Windows [Version 6.1.7601]
    Copyright (c) 2009 Microsoft Corporation.  All rights reserved.
    
    C:\Users\montoya>python
    Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)]
     on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> print('Hola')
    Hola
    >>>
    ```
    
    ```console   
    C:\Users\montoya>python
    Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)]
     on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> def add_two(x, y):
    ...     return x + y
    ...
    >>> add_two (5, 7)
    12
    >>>
    ```
    
    
4. To exit python console type ``exit()``

    ```console
    Microsoft Windows [Version 6.1.7601]
    Copyright (c) 2009 Microsoft Corporation.  All rights reserved.
    
    C:\Users\montoya>python
    Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)]
     on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> print('Hola')
    Hola
    >>>
    ```





[Video: Running python from your console](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9548086?start=0)  
[Video: Running python](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9548090?start=0)


## What is a virtualenv

* How to install packages by using the console: ``pip install package-name``

```console
C:\Users\montoya>pip install requests
Requirement already satisfied: requests in c:\users\montoya\appdata\local\progra
ms\python\python36-32\lib\site-packages (2.18.4)
Requirement already satisfied: certifi>=2017.4.17 in c:\users\montoya\appdata\lo
cal\programs\python\python36-32\lib\site-packages (from requests) (2018.4.16)
Requirement already satisfied: chardet<3.1.0,>=3.0.2 in c:\users\montoya\appdata
\local\programs\python\python36-32\lib\site-packages (from requests) (3.0.4)
Requirement already satisfied: urllib3<1.23,>=1.21.1 in c:\users\montoya\appdata
\local\programs\python\python36-32\lib\site-packages (from requests) (1.22)
Requirement already satisfied: idna<2.7,>=2.5 in c:\users\montoya\appdata\local\
programs\python\python36-32\lib\site-packages (from requests) (2.6)

C:\Users\montoya>
```

>**NOTE:** In the example above the requests package and all the dependencies are already installed, therefore its shows the message "Requirement already satisfied".

* How to check which packages are installed: ``pip freeze``

```console
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Users\montoya>pip freeze
astroid==1.6.1
beautifulsoup4==4.6.0
certifi==2018.4.16
chardet==3.0.4
click==6.7
colorama==0.3.9
Flask==0.12.2
idna==2.6
isort==4.3.4
itsdangerous==0.24
Jinja2==2.10
lazy-object-proxy==1.3.1
MarkupSafe==1.0
mccabe==0.6.1
pylint==1.8.2
pytz==2018.4
requests==2.18.4
six==1.11.0
urllib3==1.22
virtualenv==15.1.0
Werkzeug==0.14.1
wrapt==1.10.11

C:\Users\montoya>
```


* Installing the ``virtualenv`` package: ``pip install virtualenv``

```console
C:\Users\montoya>pip install virtualenv
Requirement already satisfied: virtualenv in c:\users\montoya\appdata\local\prog
rams\python\python36-32\lib\site-packages (15.1.0)

C:\Users\montoya>
```

* Create a virtualenv: 

    * On Linux and Mac: ``virtualenv venv --python=python3.7``
    * On Windows: ``virtualenv --python "C:\Users\Gabriel\AppData\Local\Programs\Python\Python36-32\python.exe" venv``
    
    >**NOTE:** On Windows, you have to set the path to where python you want to use is located.

    
```console
Using base prefix 'C:\\Users\\Gabriel\\AppData\\Local\\Programs\\Python\\Python36-32'
New python executable in C:\Users\Gabriel\Documents\Projects\curso_rest_api_flask\section_04_Flask_Restful\venv\Scripts\python.exe
Installing setuptools, pip, wheel...done.
Running virtualenv with interpreter C:\Users\Gabriel\AppData\Local\Programs\Python\Python36-32\python.exe
```

* To activate the virtual environment: 

Windows: ``.\venv\Scripts\activate.bat``  
Linux: ``source ./venv/bin/activate``  
The following command runs only in Linux and shows you the location of a file: ``which python3.6``


```console
C:\Users\montoya\Desktop\CursoPython\Section_13_python_on_console_and_dependenci
es>.\venv\Scripts\activate.bat

(venv) C:\Users\montoya\Desktop\CursoPython\Section_13_python_on_console_and_dep
endencies>
```


* To exit from the virtual environment: ``deactivate``

```console
(venv) C:\Users\montoya\Desktop\CursoPython\Section_13_python_on_console_and_dep
endencies>deactivate
C:\Users\montoya\Desktop\CursoPython\Section_13_python_on_console_and_dependenci
es>
```

[Video: What is a virtualenv](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9548092?start=0)


## Navigating the terminal and using virtualenv

Al trabajar con ``virtualenv`` es recomendable tener un archivo ``requirements.txt`` que contiene todas las librerias instaladas.

Al ejecutar este comando se instalan todas las librerias listadas en el archivo.

``pip install -r requirements.txt``

[Video: navigating the terminal and using virtualenv ](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9548094?start=0)


## Usando Pipenv

Para poder usar ``Pipenv`` es necesario borrar la carpeta del ``virtualenv``.

Luego se debe instalar ``pipenv``: ``pip install pipenv``  



> **NOTA:** para actualizar la version de pip: ``pip install --upgrade pip``


[Video: using Pipenv](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9548096?start=0)


## References

[How to set the path and environment variables in Windows](https://www.computerhope.com/issues/ch000549.htm)  


