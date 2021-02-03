from flask import Flask, make_response, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'


def write_to_file(*args):
    with open('history.txt', 'a') as f:
        list_to_write = [str(x) for x in [*args]]
        if len(list_to_write) == 4:
            f.write(', '.join(list_to_write))
            f.write('\n')


def get_request(currency):
    response = requests.get('https://api.exchangeratesapi.io/latest')
    response_json = response.json()
    rates = response_json["rates"]
    return rates[currency]


@app.route('/eur_to_usd/<int:amount>')
def eur_to_usd(amount):
    rate = get_request('USD')
    converted_amount = amount * rate
    write_to_file('USD', rate, amount, round(converted_amount, 4))
    return str(converted_amount)


@app.route('/eur_to_gbp/<int:amount>')
def eur_to_gbp(amount):
    rate = get_request('GBP')
    converted_amount = amount * rate
    write_to_file('GBP', rate, amount, round(converted_amount, 4))
    return str(converted_amount)


@app.route('/eur_to_php/<int:amount>')
def eur_to_php(amount):
    rate = get_request('PHP')
    converted_amount = amount * rate
    write_to_file('PHP', rate, amount, round(converted_amount, 4))
    return str(converted_amount)


@app.route('/history/')
def history():
    with open("history.txt", 'r') as f:
        file_content = f.readlines()
    return render_template('temp_1.html', file_content=file_content)


if __name__ == '__main__':
    app.run(debug=True)
