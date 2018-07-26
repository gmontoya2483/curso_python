from flask import Flask, render_template, request, redirect, url_for

# Definir el nombre de la applicación Flask
app = Flask(__name__)

posts = {
    0:  {
        'id': 0,
        'title': 'Hello, world',
        'content': 'This is my first blog post!'
    }
}


# Definir la primer url de la applicación
@app.route('/')
def home():
    return render_template('home.jinja2', posts= posts)


@app.route('/post/<int:post_id>') # /post/0
def post(post_id):
    post = posts.get(post_id)
    if not post:
        return render_template('404.html', message=f'A post with id { post_id }  was not found.'), 404
    return render_template('post.html', post=post)


@app.route('/post/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_id = len(posts)
        posts[post_id] = {'id': post_id, 'title': title, 'content': content}
        return redirect(url_for('post', post_id=post_id))

    # si es GET hace el render del form
    return render_template('create.jinja2')


# Ejecutar la applicacion
if __name__ == '__main__':
    app.run(debug=True)
