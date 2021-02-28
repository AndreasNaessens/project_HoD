import flask
import requests
import json
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# api-endpoint
response = requests.get("https://epistat.sciensano.be/Data/COVID19BE_CASES_AGESEX.json")
data = response.json()

@app.route('/', methods=['GET'])
def home():
    #getting specific data out of a API
    return data[1]["PROVINCE"]

@app.route('/all', methods=['GET'])
def total_cases_in_province():
    all = list(filter(lambda x: (x["PROVINCE"] if "PROVINCE" in x else None) == "OostVlaanderen", data))
    total = 0
    for case in all:
        total += case['CASES']
    return str(total)

@app.route('/average', methods=['GET'])
def average_cases_in_province():
    all = list(filter(lambda x: (x["PROVINCE"] if "PROVINCE" in x else None) == "Brussels", data))
    total = 0
    i = 0
    for case in all:
        i += 1
        total += case['CASES']
    avg_value = total / i
    return str(round(avg_value, 2))

app.run()

