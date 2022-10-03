from flask import Flask , render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
app=Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)
def index():
	return render_template('index.html')
def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

@app.route('/create', methods=('GET', 'POST'))
def create():
    return render_template('create.html')
	
