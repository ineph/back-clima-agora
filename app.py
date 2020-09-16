from cachetools import TTLCache
import requests
import json
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

weatherbit_api_base = 'http://api.weatherbit.io/v2.0/'
weatherbit_api_key = '55122f2c18204337a2a823a4e91778fa'
# forecast_weather = 'forecast/daily'
# current_weather = 'current'

route_forecast_cache = {}
route_current_cache = {}
cache = TTLCache(maxsize=80, ttl=600)


@app.route("/<route>")
def get_method(route):

    place = request.args.get('city')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    coordinates = str(lat) + str(lon)
    str_coordinates = coordinates.replace('-', 'm')
    str_place = str(place)

    if route == 'forecast':
        route = 'forecast/daily'

    if place:
        if place in cache:
            print('USED CACHE: place')
            return(cache[str_place])
        else:
            print('AAAAAAOOOOOOOOOOO')
            print(route)
            response = requests.get(weatherbit_api_base + route + '?city=' + place + '&lang=pt&days=7&key=' + weatherbit_api_key)
            cache[str_place] = response.json()
            show = response.json()
            print('NOT USED CACHE: place')
            return(show)
    else:
        if str_coordinates in cache:
            print('USED CACHE TO COORDINATES')
            return(cache[str_coordinates])
        else:
            response = requests.get(weatherbit_api_base + route + '?lat=' + lat + '&lon=' + lon + '&lang=pt&days=7&key=' + weatherbit_api_key)
            cache[str_coordinates] = response.json()
            show = response.json()
            print('NOT USED CACE TO CORDINATES')
            return(show)

# @app.route("/current")
# def get_current():
#     place = request.args.get('city')
#     lat = request.args.get('lat')
#     lon = request.args.get('lon')
#     coordinates = str(lat) + str(lon)
#     str_coordinates = coordinates.replace('-', 'm')

#     if place:
#         if place in cache:
#             return(cache[place])
#         else:
#             response = requests.get(weatherbit_api_base + current_weather + '?city=' + place + '&lang=pt&days=7&key=' + weatherbit_api_key)
#             cache[place] = response.json()
#             show = response.json()
#             return(show)
#     else:
#         if str_coordinates in cache:
#             return(cache[str_coordinates])
#         else:
#             response = requests.get(weatherbit_api_base + current_weather + '?lat=' + lat + '&lon=' + lon + '&lang=pt&days=7&key=' + weatherbit_api_key)
#             cache[str_coordinates] = response.json()
#             show = response.json()
#             return(show)

if __name__ == "__main__":
    app.run()