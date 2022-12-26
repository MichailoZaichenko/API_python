import json, requests
# TODO Insert your api key from open weather
from keys import API_KEY

URL = 'https://api.openweathermap.org/data/2.5/weather'
QUERY_CITY = f"?q={0}&appid={1}"
city = input("City: ")
request = URL + QUERY_CITY.format(city, API_KEY)