https://developer.accuweather.com/apis
https://www.geoplugin.com/

# (REQUESTS) Biblioteca para fazer requisições HTTP

# (JSON) Biblioteca para trabalhar com dados JSON (JSON = Dicionario em PY, converte todos dados em 'str' para ser aceito em qualquer linguagem)

# (PPRINT) Organiza e indenta a saída para ser mais fácil de ler.
import requests
import json
import pprint



# Trocar API Key quando expirar prazo (API MYAPPS) no AccuWeather
accueweatherAPIKEY = 'gpu6gl6y2O4Zrbh82ih49QqkwsBSwaQH' 



# Request R pega a latitude e longitude do local do usuario
r = requests.get('http://www.geoplugin.net/json.gp')
# Verificação se foi sucesso em pegar os dados
if (r.status_code!= 200):
    print('Não foi possivel obter a localização (R)')
else:
    localizacao = (json.loads(r.text))
# print(pprint.pprint(json.loads(r.text))) - apenas verificar se deu certo e ver as informaçoes do dicionario identado
    lat = localizacao['geoplugin_latitude']
    long = localizacao['geoplugin_longitude']




# Buscando Location API, saber a localização e informaçoes do local (ex. São Paulo - SP - Brasil - America do Sul) com a (APIKEY e Lat e Long) - Geopositions AccueWather
    locationAPIUrl = (
        f"http://dataservice.accuweather.com/locations/v1/cities/geoposition/search"
        f"?apikey={accueweatherAPIKEY}&q={lat},{long}&language=pt-br"
    )
    r2 = requests.get(locationAPIUrl)
# Faz a verificação se foi possivel obter informações do local
    if (r2.status_code != 200):
        print('Não foi possivel obter o codigo do local (R2)')
    else:
        location_response = json.loads(r2.text)
# print(pprint.pprint(json.loads(r2.text))) - apenas verificar se deu certo e ver as informaçoes do dicionario identado

# Define as variveias para Cidade - Estado - Pais
        nome_local = location_response['LocalizedName'], location_response['AdministrativeArea']['LocalizedName'], location_response['Country']['LocalizedName']
        codigo_local = location_response['Key']
        print('Obtendo Clima do Local:', nome_local)



# Buscando clima  do local, Current Condition AccueWather
        current_conditionsAPIUrl =(
            f"http://dataservice.accuweather.com/currentconditions/v1/{codigo_local}"
            f"?apikey={accueweatherAPIKEY}&language=pt-br"
        )
        r3 = requests.get(current_conditionsAPIUrl)

        if (r3.status_code != 200):
            print('Não foi possível obter condição Local (R3)')
        else:
            current_conditions_response = json.loads(r3.text)
# print(pprint.pprint(json.loads(r3.text))) - apenas verificar se deu certo e ver as informaçoes do dicionario identado
            