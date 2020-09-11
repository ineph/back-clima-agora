import requests
import json
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
weatherbit_api = 'http://api.weatherbit.io/v2.0/forecast/daily'
weatherbit_api_key = '55122f2c18204337a2a823a4e91778fa'
# response = requests.get(base_api_url + '?city=Raleigh,NC&lang=pt&days=7&key=' + api_key)

openweather_api_key = 'db30105f4c7958ae5633b69b98dce69f'
response = 'http://api.openweathermap.org/data/2.5/weather?q={Aracatuba}&appid={' + openweather_api_key + '}'
testemap = 'http://maps.openweathermap.org/maps/2.0/weather/TA2/{z}/{x}/{y}?date=1527811200&opacity=0.9&fill_bound=true&appid={db30105f4c7958ae5633b69b98dce69f}'

def jsonprint(obj):
    text = json.dumps(obj,sort_keys= True, indent= 4)
    return(text)

@app.route("/")
def dummy_api():
    show = testemap.json()
    return(show)


if __name__ == "__main__":
    app.run()