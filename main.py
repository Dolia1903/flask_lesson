from flask import Flask, make_response
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/eur_to_usd/<int:amount>')
def eur_to_usd(amount):
    response = requests.get('https://api.exchangeratesapi.io/latest')
    response_json = response.json()
    rates = response_json["rates"]
    converted_amount = amount * rates["USD"]
    f = open("history.html", "a")
    f.writelines(str(["USD", rates["USD"], amount, converted_amount]))
    f.close()
    return str(converted_amount)


@app.route('/eur_to_gbp/<int:amount>')
def eur_to_gbp(amount):
    response = requests.get('https://api.exchangeratesapi.io/latest')
    response_json = response.json()
    rates = response_json["rates"]
    converted_amount = amount * rates["GBP"]
    f = open("history.html", "a")
    f.writelines(str(["GBP", rates["GBP"], amount, converted_amount]))
    f.close()
    return str(converted_amount)


@app.route('/eur_to_php/<int:amount>')
def eur_to_php(amount):
    response = requests.get('https://api.exchangeratesapi.io/latest')
    response_json = response.json()
    rates = response_json["rates"]
    converted_amount = amount * rates["PHP"]
    f = open("history.html", "a")
    f.writelines(str(["PHP", rates["PHP"], amount, converted_amount]))
    f.close()
    return str(converted_amount)


@app.route('/history/')
def history():
    with open("history.html") as f:
        file_content = f.read()
    return file_content


if __name__ == '__main__':
    history_file = "history.html"
    app.run(debug=True)
