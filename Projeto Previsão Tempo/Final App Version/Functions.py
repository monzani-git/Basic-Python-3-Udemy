import requests
import json
import datetime
import pprint

accuweatherAPIKEY = 'gpu6gl6y2O4Zrbh82ih49QqkwsBSwaQH' #Trocar API Key quando expirar prazo

def get_coordinates():

    r = requests.get('http://www.geoplugin.net/json.gp')

    if (r.status_code  != 200):
        print('Não foi possivel obter as coordenadas (get_coordinates)')
        return None
    else:
        try:
            localizacao = (json.loads(r.text))
            coordenadas = {}
            coordenadas ['lat'] = localizacao['geoplugin_latitude']
            coordenadas ['long'] = localizacao['geoplugin_longitude']
            return coordenadas
        except:
            return None
    
def get_local_code(lat,long):
    locationAPIUrl = (
        f"http://dataservice.accuweather.com/locations/v1/cities/geoposition/search"
        f"?apikey={accuweatherAPIKEY}&q={lat},{long}&language=pt-br"
    )
    
    r = requests.get(locationAPIUrl)

    if (r.status_code != 200):
        print('Não foi possivel obter a localização (get_local_code)')
        return None
    else:
        try:
            location_response = json.loads(r.text)
            info_local = {}
            info_local ['nome_local']  = location_response['LocalizedName'] + " - " + location_response['AdministrativeArea']['LocalizedName'] + " - " + location_response['Country']['LocalizedName']
            info_local ['codigo_local'] = location_response['Key']
            return info_local
        except:
            return None

def get_present_condition(codigo_local, nome_local):
        current_conditionsAPIUrl =(
            f"http://dataservice.accuweather.com/currentconditions/v1/{codigo_local}"
            f"?apikey={accuweatherAPIKEY}&language=pt-br"
        )
        r = requests.get(current_conditionsAPIUrl)
        if (r.status_code != 200):
            print('Não foi possível obter Clima Local (get_present_condition)')
            return None
        else:
            try:
                current_conditions_response = json.loads(r.text)
                info_clima = {}
                info_clima ['text_clima'] = current_conditions_response[0]['WeatherText']
                info_clima ['temperatura'] = current_conditions_response[0]['Temperature']['Metric']['Value']
                info_clima ['nome_local'] = nome_local
                return info_clima
            except:
                return None

def get_daily (codigo_local):
    DailyAPIUrl = (
        f"http://dataservice.accuweather.com/forecasts/v1/daily/5day/{codigo_local}"
        f"?apikey={accuweatherAPIKEY}&language=pt-br"
    )
    r = requests.get(DailyAPIUrl)
    if (r.status_code != 200):
        print('Não foi possivel obter clima da semana (get_daily)')
        return  None  
    else:
        try:
            DailyAPIUrl = json.loads(r.text)
            info_semana = []
            for dia in DailyAPIUrl['DailyForecasts']:
                ClimaDia = {}
                ClimaDia ['max'] = dia['Temperature']['Maximum']['Value']
                ClimaDia ['min'] = dia['Temperature']['Minimum']['Value']
                ClimaDia ['clima'] = dia['Day']['IconPhrase']
                ClimaDia ['dia'] = dia['EpochDate']
                info_semana.append(ClimaDia)
            return info_semana
        except:
            return None