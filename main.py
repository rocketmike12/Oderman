from flask import Flask, render_template, request
import sqlite3
import json

app = Flask(__name__, template_folder='templates', static_folder='static')
feedback_filename = 'feedback.json'
app.config['SECRET_KEY'] = 'lemonade'


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    context = {
        'title': 'Oderman'
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


@app.route('/order')
def order():
    conn = get_db_connection()
    menu_list = conn.execute('SELECT * FROM menu').fetchall()
    conn.close()
    price = 0
    for i in range(len(menu_list)):
        if not int(request.args.get(f"{i + 1}")) == 0:
            price += int(request.args.get(f"{i + 1}")) * menu_list[i]['price']
    return render_template('pay.html', price=price, title='Pay for your order')


@app.route('/feedback')
def feedback():
    conn = get_db_connection()
    menu_list = conn.execute('SELECT * FROM menu').fetchall()
    conn.close()

    context = {
        'title': 'Feedback',
        'menu': menu_list
    }

    return render_template('feedback.html', **context)


@app.route('/thank_you_feedback')
def thank_you():
    feedback_name = request.args.get('name')
    feedback_rating = request.args.get('rating')
    feedback_comment = request.args.get('comment')

    with open(feedback_filename, 'r') as f:
        feedback_json = json.loads(f.read())
    if feedback_name is not None and feedback_rating is not None:
        with open(feedback_filename, 'w') as f:
            feedback_json.append({'name': feedback_name, 'rating': feedback_rating, 'comment': '' if feedback_comment is None else feedback_comment})
            f.write(json.dumps(feedback_json))

    return render_template('thank_you_feedback.html', **{'title': 'Thank You'})


app.run(debug=True)
