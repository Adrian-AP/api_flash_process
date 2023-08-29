
## Libraries ##

import requests
import pandas as pd
import shutil

## Functions to move files ##

def mover_archivo(origen, destino):
    try:
        shutil.move(origen, destino)
        print(f"Archivo movido de {origen} a {destino}")
        
    except Exception as e:
        print(f"Error al mover el archivo: {e}")


## Requests ##


def geo_information(url_s = str, json_s = dict):

    response = requests.post(url_s, json=json_s)
    prediction = response.json()
    print(pd.read_json(prediction))


def graphic_country_life(url_s = str, json_s = dict):
    
    rexx = requests.get(url_s, json=json_s)
    
    # Saving into png
    with open("./output.png", "wb") as f:
        f.write(rexx.content)
    
    

if __name__ == "__main__":
    
    url_sendind = "http://localhost:8052/continent_pop"
    url_sending_two = "http://localhost:8052/pais_life"
    
    data_fi = {
    "continent": "Asia",
    "year": 1992
     }
    
    
    data_se = {
    "country": "Japan",
    "title": "Japan LifeExp evolution",
    }


    geo_information(url_sendind, data_fi)

    graphic_country_life(url_s = url_sending_two, json_s = data_se)
    
        
        
    route = "output.png"
    route_two = "api_flash_process/2_Functions/respones/static/output.png"
    
    mover_archivo(route, route_two)