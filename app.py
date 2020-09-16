
import requests
import json
from cachetools import TTLCache
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

weatherbit_api_base = 'http://api.weatherbit.io/v2.0/'
weatherbit_api_key = '55122f2c18204337a2a823a4e91778fa'

cache_forecast = TTLCache(maxsize=80, ttl=600)
cache_current = TTLCache(maxsize=80, ttl=600)


@app.route("/current")
def get_current():
    place = request.args.get('city')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    coordinates = str(lat) + str(lon)
    str_coordinates = coordinates.replace('-', 'm')

    if place:
        if place in cache_current:
            print('used cache_current current place')
            return(cache_current[place])
        else:
            response = requests.get(weatherbit_api_base + 'current' + '?city=' + place + '&lang=pt&days=7&key=' + weatherbit_api_key)
            cache_current[place] = response.json()
            show = response.json()
            return(show)
    else:
        if str_coordinates in cache_current:
            print('used cache current coordinates')
            return(cache_current[str_coordinates])
        else:
            response = requests.get(weatherbit_api_base + 'current' + '?lat=' + lat + '&lon=' + lon + '&lang=pt&days=7&key=' + weatherbit_api_key)
            cache_current[str_coordinates] = response.json()
            show = response.json()
            return(show)

@app.route("/forecast")
def get_forecast():
    place = request.args.get('city')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    coordinates = str(lat) + str(lon)
    str_coordinates = coordinates.replace('-', 'm')

    if place:
        if place in cache_forecast:
            print('used cache forecast place')
            return(cache_forecast[place])
        else:
            response = requests.get(weatherbit_api_base + 'forecast/daily' + '?city=' + place + '&lang=pt&days=7&key=' + weatherbit_api_key)
            cache_forecast[place] = response.json()
            show = response.json()
            return(show)
    else:
        if str_coordinates in cache_forecast:
            print('used cache fprecast coords')
            return(cache_forecast[str_coordinates])
        else:
            response = requests.get(weatherbit_api_base + 'forecast/daily' + '?lat=' + lat + '&lon=' + lon + '&lang=pt&days=7&key=' + weatherbit_api_key)
            cache_forecast[str_coordinates] = response.json()
            show = response.json()
            return(show)

if __name__ == "__main__":
    app.run()