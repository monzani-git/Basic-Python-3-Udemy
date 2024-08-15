# Documentação do Código

Este documento fornece uma visão geral sobre o código que utiliza APIs para obter dados de localização e clima.

# Bibliotecas Utilizadas

- **requests**: Biblioteca para fazer requisições HTTP.
- **json**: Biblioteca para trabalhar com dados JSON (JSON = Dicionário em Python, converte todos dados em 'str' para ser aceito em qualquer linguagem).
- **pprint**: Biblioteca para organizar e indentar a saída, facilitando a leitura.

```python
import requests
import json
import pprint
```

# Configurações

## API Key

Troque a `API Key` quando o prazo expirar (API MYAPPS) no AccuWeather:

```python
accueweatherAPIKEY = 'gpu6gl6y2O4Zrbh82ih49QqkwsBSwaQH'
```

# Etapas do Código

## 1. Obter Latitude e Longitude do Usuário

Realiza uma requisição para obter a latitude e longitude do local do usuário.

```python
r = requests.get('http://www.geoplugin.net/json.gp')
```

**Verificação de Sucesso**: Se a requisição não for bem-sucedida, uma mensagem de erro será exibida.

```python
if (r.status_code != 200):
    print('Não foi possível obter a localização (R)')
else:
    localizacao = (json.loads(r.text))
    lat = localizacao['geoplugin_latitude']
    long = localizacao['geoplugin_longitude']
```

## 2. Buscar Informações de Localização

Usa a latitude e longitude obtidas para buscar informações detalhadas sobre a localização (cidade, estado, país) com a API AccuWeather.

```python
locationAPIUrl = (
    f"http://dataservice.accuweather.com/locations/v1/cities/geoposition/search"
    f"?apikey={accueweatherAPIKEY}&q={lat},{long}&language=pt-br"
)
r2 = requests.get(locationAPIUrl)
```

**Verificação de Sucesso**: Se a requisição não for bem-sucedida, uma mensagem de erro será exibida.

```python
if (r2.status_code != 200):
    print('Não foi possível obter o código do local (R2)')
else:
    location_response = json.loads(r2.text)
    nome_local = location_response['LocalizedName'], location_response['AdministrativeArea']['LocalizedName'], location_response['Country']['LocalizedName']
    codigo_local = location_response['Key']
    print('Obtendo Clima do Local:', nome_local)
```

## 3. Obter Condições Climáticas Atuais

Busca as condições climáticas atuais para a localização obtida usando a API AccuWeather.

```python
current_conditionsAPIUrl =(
    f"http://dataservice.accuweather.com/currentconditions/v1/{codigo_local}"
    f"?apikey={accueweatherAPIKEY}&language=pt-br"
)
r3 = requests.get(current_conditionsAPIUrl)
```

**Verificação de Sucesso**: Se a requisição não for bem-sucedida, uma mensagem de erro será exibida.

```python
if (r3.status_code != 200):
    print('Não foi possível obter condição Local (R3)')
else:
    current_conditions_response = json.loads(r3.text)
```

# Observações

- As chamadas à API são feitas usando a biblioteca `requests`.
- O `pprint` é usado para formatar a saída para uma melhor leitura. Ex. print(pprint.pprint(json.loads(r.text)))

**Links Úteis**:
- [AccuWeather API Documentation](https://developer.accuweather.com/apis)
- [GeoPlugin](https://www.geoplugin.com/)