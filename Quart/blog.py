from quart import (
    abort, redirect, render_template, request, session,
    url_for, g, flash
)
from pathlib import Path
from sqlite3 import dbapi2 as sqlite3
from quart.app import Quart

app = Quart(__name__)


app.config.update({
    'DATABASE': app.root_path / 'blog.db',
})


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.route('/', methods=['GET'])
async def posts():
    db = get_db()
    cur = db.execute(
        """SELECT title, text
              FROM post
          ORDER BY id DESC""",
    )
    posts = cur.fetchall()
    return await render_template('posts.html', posts=posts)


def connect_db():
    engine = sqlite3.connect(app.config['DATABASE'])
    engine.row_factory = sqlite3.Row
    return engine


@app.cli.command('init_db')
def init_db():
    """Create an empty database."""
    db = connect_db()
    with open(Path(__file__).parent / 'schema.sql', mode='r') as file_:
        db.cursor().executescript(file_.read())
    db.commit()


app.config.update({
    'SECRET_KEY': 'development key',
    'USERNAME': 'admin',
    'PASSWORD': 'default',
})


@app.route('/', methods=['POST'])
async def create():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    form = await request.form
    db.execute(
        "INSERT INTO post (title, text) VALUES (?, ?)",
        [form['title'], form['text']],
    )
    db.commit()
    return redirect(url_for('posts'))


@app.route('/login/', methods=['GET', 'POST'])
async def login():
    error = None
    if request.method == 'POST':
        form = await request.form
        if form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            return redirect(url_for('posts'))
    return await render_template('login.html', error=error)


@app.route('/logout/')
async def logout():
    session.pop('logged_in', None)
    await flash('You were logged out')
    return redirect(url_for('posts'))
