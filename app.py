from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3
import os

app = Flask(__name__)
DATABASE = 'quotes.db'

# DB 연결 함수
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

# 요청 끝날 때 DB 연결 종료
@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db:
        db.close()

# DB 초기화 함수
def init_db():
    with app.app_context():
        db = get_db()
        with open('schema.sql', mode='r', encoding='utf-8') as f:
            db.executescript(f.read())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_quote():
    quote = request.form['quote']
    if quote:
        db = get_db()
        db.execute("INSERT INTO quotes (text) VALUES (?)", (quote,))
        db.commit()
    return redirect(url_for('show_quotes'))

@app.route('/quotes')
def show_quotes():
    db = get_db()
    cur = db.execute("SELECT id, text FROM quotes ORDER BY id DESC")
    quotes = cur.fetchall()
    return render_template('quotes.html', quotes=quotes)

if __name__ == '__main__':
    # 처음 실행 시 DB 초기화
    if not os.path.exists(DATABASE):
        init_db()
    app.run(debug=True)
