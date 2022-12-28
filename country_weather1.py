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

def current_weather(q: str = city, appid: str = API_KEY) -> dict:
    try:
        request = requests.get(URL, params=locals())
        print(city)
        data = request.json()
        print('\/\/\/\/\/\/\/', end ='')
        descript = data.get("weather")[0].get("description")
        print(descript, end = '')
        print('\/\/\/\/\/\/\/')

        temp = data.get("main").get("temp")
        temp = round(temp-273)
        print(f"Температура {temp} °C")

        hum = data.get("main").get("humidity")
        print(f"Влажность", hum,"%")

        wind_speed = data.get("wind").get("speed")
        print('Скорость ветра', wind_speed, "m/s")
    except TypeError:
        print("Введите название города правильно!")
current_weather()