import json, requests
# TODO Insert youre API_KEY from ...
from keys import API_KEY

URL ='https://api.openweathermap.org/data/2.5/weather?'
QUERY_CITY = f"?q={0}&appid={1}"
par = {
	"lang":"ru",
	"lat": 53,
	"lon": 30,
	"appid": "84061a2a5ff54b490d63bd38d557b06d",
	"units": "metric"
}
city = input('City: ')

