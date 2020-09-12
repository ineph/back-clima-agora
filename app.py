import requests
import json
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

weatherbit_api = 'http://api.weatherbit.io/v2.0/forecast/daily'
weatherbit_api_key = '55122f2c18204337a2a823a4e91778fa'

def jsonprint(obj):
    text = json.dumps(obj,sort_keys= True, indent= 4)
    return(text)

@app.route("/")
def call_api():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    response = requests.get(weatherbit_api + '?lat='+lat+'&lon='+lon+'&lang=pt&days=7&key=' + weatherbit_api_key)
    show = response.json()
    return(show)


if __name__ == "__main__":
    app.run()