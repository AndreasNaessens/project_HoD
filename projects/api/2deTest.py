import os
import flask
import requests
from flask import Flask
from flask import redirect
from flask import render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True
basedir = os.path.abspath(os.path.dirname(__file__))
# api-endpoint
response = requests.get("https://epistat.sciensano.be/Data/COVID19BE_CASES_AGESEX.json")
data = response.json()

@app.route('/', methods=['GET'])
def home():
    #getting specific data out of a API
    let = set()
    for s in data:
        if 'PROVINCE' in s:
            let.add(s['PROVINCE'])
    return render_template('Home.html', Full_data=data, Province=let)

@app.route('/total/province/<Province>', methods=['GET'])
def total_cases_in_province(Province):

    all = list(filter(lambda x: (x["PROVINCE"] if "PROVINCE" in x else None) == Province, data))
    total = 0
    for case in all:
        total += case['CASES']
    return render_template('total.html', Total_values = str(total), Name_Province= Province)

@app.route('/average/province/<Province>', methods=['GET'])
def average_cases_in_province(Province):
    all = list(filter(lambda x: (x["PROVINCE"] if "PROVINCE" in x else None) == Province, data))
    total = 0
    i = 0
    for case in all:
        i += 1
        total += case['CASES']
    avg_value = total / i
    return render_template('average.html', avg_values = str(round(avg_value, 2)), Name_Province= Province)


if __name__ == '__main__':
    app.run()


