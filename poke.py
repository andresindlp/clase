# Descarga listado pokemon en formato JSON
# # Tareas buscar en Internet para que sirve las librerias request y python
# # Opcional: Visualizar un listado con sólo los nombres de los pokemon
# # consultando esta página https://daviddelatorre.me/json-con-python-obtener-los-datos/

import requests
import json

url="https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
response = requests.get(url)
data = json.loads(response.text)

print(data["pokemon"])


##########################
for i in data["pokemon"]:
    id, name = i["id"], i["name"]
    print(str(id) + ": " + str(name))

##########################