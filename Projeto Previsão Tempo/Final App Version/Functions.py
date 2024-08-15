import requests
import json
import pprint

accueweatherAPIKEY = 'gpu6gl6y2O4Zrbh82ih49QqkwsBSwaQH' #Trocar API Key quando expirar prazo

r = requests.get('http://www.geoplugin.net/json.gp')

if (r.status_code!= 200):
    print('Não foi possivel obter a localização (R)')
else:
    localizacao = (json.loads(r.text))
    lat = localizacao['geoplugin_latitude']
    long = localizacao['geoplugin_longitude']
    
    locationAPIUrl = (
        f"http://dataservice.accuweather.com/locations/v1/cities/geoposition/search"
        f"?apikey={accueweatherAPIKEY}&q={lat},{long}&language=pt-br"
    )
    
    r2 = requests.get(locationAPIUrl)

    if (r2.status_code != 200):
        print('Não foi possivel obter o codigo do local (R2)')
    else:
        location_response = json.loads(r2.text)
        
        nome_local = location_response['LocalizedName'], location_response['AdministrativeArea']['LocalizedName'], location_response['Country']['LocalizedName']
        codigo_local = location_response['Key']
        
        print('Obtendo Clima do Local:', nome_local)
        
        current_conditionsAPIUrl =(
            f"http://dataservice.accuweather.com/currentconditions/v1/{codigo_local}"
            f"?apikey={accueweatherAPIKEY}&language=pt-br"
        )
        
        r3 = requests.get(current_conditionsAPIUrl)
        if (r3.status_code != 200):
            print('Não foi possível obter condição Local (R3)')
        else:
            current_conditions_response = json.loads(r3.text)
            text_clima = current_conditions_response[0]['WeatherText']
            temperatura = current_conditions_response[0]['Temperature']['Metric']['Value']
            
            print('Clima no momento: ', text_clima)
            print('Temperatura: '+ str(temperatura) + ' Graus Celsius')