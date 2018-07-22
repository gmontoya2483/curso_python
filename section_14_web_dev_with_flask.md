# Section 14: Web development with Flask

[VOLVER a README.md](README.md)

## Indice

* [Introduction to this section](#introduction-to-this-section)
* [Nuestro primer end point](#nuestro-primer-end-point)
* [Devolviendo información con Flask](#devolviendo-información-con-flask)
* [Rendering HTML](#rendering-html)
* [Paginas de Error y herencia en Jinja2](#paginas-de-error-y-herencia-en-jinja2)


## Introduction to this section

[Video: Introduction to this section](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9552012?start=0)


## Setting up the project  with pipenv

Dentro de la carpeta donde se encuentra el proyecto ejecutar:

``pipenv install Flask``

En este caso el entorno virtual se creo en:

```console
Virtualenv location: C:\Users\Gabriel\.virtualenvs\Section_14_web_dev_with_flask-84u-e2P_
Creating a Pipfile for this project...
Installing Flask...
```
Además, este comado genera los archivos ``Pipfile`` y ``Pipfile.lock``


[Video: Setting up the project  with pipenv](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9552016?start=0)



## Nuestro primer end point

```python
from flask import Flask

# Definir el nombre de la applicación Flask
app = Flask(__name__)


# Definir la primer url de la applicación
@app.route('/')
def home():
    return 'Hello, world!'


# Ejecutar la applicacion
if __name__ == '__main__':
    app.run(debug=True)
```

[Video: Our first end point](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9552018?start=0)


## Devolviendo información con Flask

```python
from flask import Flask

# Definir el nombre de la applicación Flask
app = Flask(__name__)

posts = {
    0:  {
        'title': 'Hello, world',
        'content': 'This is my first blog post!'
    }
}


# Definir la primer url de la applicación
@app.route('/')
def home():
    return 'Hello, world!'


@app.route('/post/<int:post_id>') # /post/0
def post(post_id):
    post = posts.get(post_id)
    return f"Post { post['title'] }, content:\n\n{ post['content'] }"
    
```

[Video: Returning information with Flask and Python](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9552020?start=0)


##  Rendering HTML

Flask busca los templates de HTML dentro de una carpeta llamada ``templates`` que tiene que ser creada almismo nivel que el archivo ``app.py``.  

```python
from flask import Flask, render_template

# Definir el nombre de la applicación Flask
app = Flask(__name__)

posts = {
    0:  {
        'title': 'Hello, world',
        'content': 'This is my first blog post!'
    }
}


# Definir la primer url de la applicación
@app.route('/')
def home():
    return 'Hello, world!'


@app.route('/post/<int:post_id>') # /post/0
def post(post_id):
    return render_template('post.html', post=posts.get(post_id))


# Ejecutar la applicacion
if __name__ == '__main__':
    app.run(debug=True)

```

post.html

```html
<!DOCTYPE html>
<html>
    <head></head>
    <body>
    <h1>{{ post['title'] }}</h1>
    <p> {{ post['content'] }}</p>

    </body>
</html>
```

[Video: Rendering HTML with Flask and Python](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9552022?start=0)


## Paginas de Error y herencia en Jinja2

* app.py

```python
from flask import Flask, render_template

# Definir el nombre de la applicación Flask
app = Flask(__name__)

posts = {
    0:  {
        'title': 'Hello, world',
        'content': 'This is my first blog post!'
    }
}


# Definir la primer url de la applicación
@app.route('/')
def home():
    return 'Hello, world!'


@app.route('/post/<int:post_id>') # /post/0
def post(post_id):
    post = posts.get(post_id)
    if not post:
        return render_template('404.html', message=f'A post with id { post_id }  was not found.')
    return render_template('post.html', post=post)


# Ejecutar la applicacion
if __name__ == '__main__':
    app.run(debug=True)

```

* base.jinja2

```html
<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body>
    {% block content %}

    {% endblock %}
</body>
</html>
```

* post.html

```html
{% extends 'base.jinja2' %}

{% block content %}
<h1>{{ post['title'] }}</h1>
<p> {{ post['content'] }}</p>
{% endblock %}
```

* 404.html

```html
{% extends 'base.jinja2' %}

{% block content %}
<h1>404 - Post not found</h1>
<p>{{ message }}</p>
{% endblock %}
```

[Video: Error pages and inheritance in jinja2](https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9552024?start=0)

