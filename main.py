from flask import Flask, make_response, render_template, g, request
import requests
import sqlite3

app = Flask(__name__)

DATABASE = '/home/dolia/PycharmProjects/Dolia1903_SQLite/venv/database.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        db = g._database = conn
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def write_to_table(currency_to, exchange_rate, amount, result):
    conn = get_db()
    cursor = conn.cursor()
    resp = cursor.execute("""
        insert into exchange (currency_to, exchange_rate, amount, result)
        values (?, ?, ?, ?)
    """, (currency_to, exchange_rate, amount, result))
    conn.commit()


def get_request(currency_to):
    response = requests.get('https://api.exchangeratesapi.io/latest')
    response_json = response.json()
    rates = response_json["rates"]
    return rates[currency_to]


@app.route('/eur_to_usd/<int:amount>')
def eur_to_usd(amount):
    rate = get_request('USD')
    result = amount * rate
    write_to_table('USD', rate, amount, round(result, 4))
    return str(result)


@app.route('/eur_to_gbp/<int:amount>')
def eur_to_gbp(amount):
    rate = get_request('GBP')
    result = amount * rate
    write_to_table('GBP', rate, amount, round(result, 4))
    return str(result)


@app.route('/eur_to_php/<int:amount>')
def eur_to_php(amount):
    rate = get_request('GBP')
    result = amount * rate
    write_to_table('PHP', rate, amount, round(result, 4))
    return str(result)


@app.route('/history/')
def history():
    conn = get_db()
    cursor = conn.cursor()
    resp = cursor.execute("""
            select currency_to, exchange_rate, amount, result
            from exchange
    """, )
    resp = resp.fetchall()
    return render_template('exchange.html', file_content=resp)


@app.route('/history/currency/<string:currency_to>')
def history_currency(currency_to):
    conn = get_db()
    cursor = conn.cursor()
    typed_currency = currency_to.upper()
    # так как я записывал через write_to_table 'USD', 'GBP', 'PHP'
    resp = cursor.execute("""
        select currency_to, exchange_rate, amount, result
        from exchange
        where currency_to = $typed_currency
    """, (typed_currency,))
    resp = resp.fetchall()
    return render_template('exchange.html', file_content=resp)


@app.route('/history/amount_gte/<int:typed_amount>')
def get_amount_gte(typed_amount):
    conn = get_db()
    cursor = conn.cursor()
    resp = cursor.execute("""
        select currency_to, exchange_rate, amount, result
        from exchange
        where amount >= $typed_amount
    """, (typed_amount,))
    resp = resp.fetchall()
    return render_template('exchange.html', file_content=resp)


@app.route('/history/statistics')
def get_history_statistics():
    conn = get_db()
    cursor = conn.cursor()
    resp = cursor.execute("""
        select currency_to, count(id), sum(result)
        from exchange
        group by currency_to
    """, )
    resp = resp.fetchall()
    return render_template('exchange.html', file_content=resp)


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
