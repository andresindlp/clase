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
    id, name, type = i["id"], i["name"], i["type"]
    tipos = ", ".join(type)
    
    
    try:
        candy = i["candy_count"]
    except:
        candy = 0

    print(str(id) + ": " + str(name) + ". Necesita " + str(candy) + " caramelos para evolucionar. " + "Tiene los siguentes tipos: " + str(tipos))
##########################