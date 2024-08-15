import requests
import json
import pprint

accueweatherAPIKEY = 'gpu6gl6y2O4Zrbh82ih49QqkwsBSwaQH' #Trocar API Key quando expirar prazo

def get_coordinates():

    r = requests.get('http://www.geoplugin.net/json.gp')

    if (r.status_code!= 200):
        print('Não foi possivel obter a localização (R)')
    else:
        localizacao = (json.loads(r.text))
        coordenadas = {}
        coordenadas ['lat'] = localizacao['geoplugin_latitude']
        coordenadas ['long'] = localizacao['geoplugin_longitude']
        return
    
def get_code_local(lat,long):
    locationAPIUrl = (
        f"http://dataservice.accuweather.com/locations/v1/cities/geoposition/search"
        f"?apikey={accueweatherAPIKEY}&q={lat},{long}&language=pt-br"
    )
    
    r = requests.get(locationAPIUrl)

    if (r.status_code != 200):
        print('Não foi possivel obter o codigo do local (R2)')
    else:
        location_response = json.loads(r.text)
        info_local = {}
        info_local ['nome_local']  = location_response['LocalizedName'], location_response['AdministrativeArea']['LocalizedName'], location_response['Country']['LocalizedName']
        info_local ['codigo_local'] = location_response['Key']
        return info_local

def get_condition_celcius(codigo_local, nome_local):
        current_conditionsAPIUrl =(
            f"http://dataservice.accuweather.com/currentconditions/v1/{codigo_local}"
            f"?apikey={accueweatherAPIKEY}&language=pt-br"
        )
        r = requests.get(current_conditionsAPIUrl)
        if (r.status_code != 200):
            print('Não foi possível obter condição Local (R3)')
        else:
            current_conditions_response = json.loads(r.text)
            info_clima = {}
            info_clima ['text_clima'] = current_conditions_response[0]['WeatherText']
            info_clima ['temperatura'] = current_conditions_response[0]['Temperature']['Metric']['Value']
            info_clima ['nome_local'] = nome_local
            return info_clima