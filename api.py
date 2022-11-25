import requests
import json

parametros={
    "apikey": "W4wo9wQ6LuW51LUxvRp0lZLALudCtLlK",
    "language": "es-ES",
    "metric": "true"
}

r = requests.get("http://dataservice.accuweather.com/forecasts/v1/daily/1day/1462817", params=parametros)


datos = r.json()
# print(json.dumps(datos, indent=3))
if r.status_code != 200:
    print("Error", str(r.status_code), ":(")
else:
    print("Elche\n" + "El mensaje de aviso es: " + str(datos["Headline"]["Text"]) + "\nLa temperatura mínima es: " + str(datos["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"]) + "\nLa temperatura máxima es: " + str(datos["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"]))

