from flask import Flask, render_template
import sqlite3

app = Flask(__name__, template_folder='templates', static_folder='static')


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    context = {
        'title': 'Oderman - pizza anywhere'
    }
    return render_template('index.html', **context)


@app.route('/menu')
def menu():
    conn = get_db_connection()
    menu_list = conn.execute('SELECT * FROM menu').fetchall()
    conn.close()
    context = {
        'menu': menu_list,
        'title': 'Oderman - Menu'
    }
    return render_template('menu.html', **context)


app.run(debug=True)
