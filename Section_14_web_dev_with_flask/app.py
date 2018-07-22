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
        return render_template('404.html', message=f'A post with id { post_id }  was not found.'), 404
    return render_template('post.html', post=post)


# Ejecutar la applicacion
if __name__ == '__main__':
    app.run(debug=True)
