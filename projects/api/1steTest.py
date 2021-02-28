










import flask
import requests
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# api-endpoint
URL = "https://epistat.sciensano.be/Data/COVID19BE_CASES_AGESEX.json"


@app.route('/', methods=['GET'])
def home():
    # location given here
    location = "Brussels"

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'PROVINCE': location}

    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)

    # extracting data in json format
    data = r.json()

    return data[1]

app.run()